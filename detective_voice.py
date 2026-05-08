"""
Detective Voice — Phase 0 Text Prototype
========================================

GDD M0~M2 단계의 핵심 가설을 텍스트만으로 검증하는 CLI 프로토타입.

검증 대상:
  H1) 사건 템플릿이 LLM의 환각을 막아주는가
  H2) 캐릭터 카드 + 거짓말 게이트가 일관된 NPC 연기로 이어지는가
  H3) Aria GM이 "답을 주지 않으면서 막히지 않게" 진행할 수 있는가

실행:
  pip install anthropic
  export ANTHROPIC_API_KEY="sk-ant-..."
  python detective_voice.py cases/last_customer.json
"""

from __future__ import annotations

import json
import os
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path

try:
    from anthropic import Anthropic
except ImportError:
    print("anthropic 패키지가 필요합니다: pip install anthropic", file=sys.stderr)
    sys.exit(1)


# ----- Config ---------------------------------------------------------------

GM_MODEL = "claude-sonnet-4-5"  # Aria 게임 마스터 (품질 우선)
NPC_MODEL = "claude-haiku-4-5"  # NPC 캐릭터 (저지연·저비용)

PROMPT_DIR = Path(__file__).parent / "prompts"
ARIA_PROMPT = (PROMPT_DIR / "aria_gm.md").read_text(encoding="utf-8")
CHARACTER_PROMPT_TEMPLATE = (PROMPT_DIR / "character.md").read_text(encoding="utf-8")


# ----- Types ----------------------------------------------------------------

@dataclass
class GameState:
    case: dict
    discovered_evidence: set[str] = field(default_factory=set)
    visited_scenes: set[str] = field(default_factory=set)
    interrogation_history: dict[str, list[dict]] = field(default_factory=dict)
    npc_anxiety: dict[str, int] = field(default_factory=dict)
    aria_history: list[dict] = field(default_factory=list)
    ended: bool = False

    @classmethod
    def load(cls, path: Path) -> "GameState":
        data = json.loads(path.read_text(encoding="utf-8"))
        gs = cls(case=data)
        for ch in data["characters"]:
            gs.npc_anxiety[ch["character_id"]] = ch["emotional_state"]["anxiety_meter_start"]
        return gs

    def evidence_summary(self) -> str:
        if not self.discovered_evidence:
            return "(아직 발견된 단서 없음)"
        lines = []
        for ev in self.case["evidence"]:
            if ev["evidence_id"] in self.discovered_evidence:
                lines.append(f"- {ev['name']}: {ev['implication']}")
        return "\n".join(lines)


# ----- Character card rendering --------------------------------------------

def render_character_prompt(character: dict) -> str:
    """간단한 mustache-스타일 치환."""
    p = CHARACTER_PROMPT_TEMPLATE
    p = p.replace("{{name}}", character["name"])
    p = p.replace("{{role}}", character["role"])
    p = p.replace("{{background}}", character["background"])
    p = p.replace("{{relationship_to_victim}}", character["relationship_to_victim"])
    p = p.replace("{{emotional_state.initial}}", character["emotional_state"]["initial"])
    p = p.replace(
        "{{emotional_state.anxiety_meter_start}}",
        str(character["emotional_state"]["anxiety_meter_start"]),
    )
    p = p.replace(
        "{{emotional_state.breaks_at}}",
        str(character["emotional_state"]["breaks_at"]),
    )
    p = p.replace(
        "{{voice_profile.speech_quirks}}",
        character["voice_profile"]["speech_quirks"],
    )

    # Truth list
    truth_block = "\n".join(f"- {t}" for t in character.get("truth", []))
    p = re.sub(
        r"\{\{#each truth\}\}.*?\{\{/each\}\}",
        truth_block or "- (특별히 솔직하게 말할 정보 없음)",
        p,
        flags=re.DOTALL,
    )

    # Lies list
    lies_blocks = []
    for lie in character.get("lies", []):
        lies_blocks.append(
            f"### 주제: {lie['topic']}\n"
            f"- **공식 답변(거짓말)**: \"{lie['lie']}\"\n"
            f"- **실제 진실(절대 먼저 말하지 마라)**: {lie['truth_behind']}\n"
            f"- **무너지는 트리거**: 플레이어가 `{lie['breaks_at']}` 증거를 제시하거나 그 내용을 정확히 인용하면, 변명 1~2회 후 무너진다."
        )
    lies_text = "\n\n".join(lies_blocks) if lies_blocks else "(거짓말하는 영역 없음 — 모든 질문에 정직하게 답한다.)"
    p = re.sub(
        r"\{\{#each lies\}\}.*?\{\{/each\}\}",
        lies_text,
        p,
        flags=re.DOTALL,
    )

    # Alibi
    p = p.replace("{{alibi.claimed}}", character["alibi"]["claimed"] or "-")
    p = p.replace("{{alibi.actual}}", character["alibi"]["actual"] or "-")
    p = p.replace("{{alibi.is_lying}}", "예" if character["alibi"]["is_lying"] else "아니오")

    return p


# ----- LLM calls -----------------------------------------------------------

def _client() -> Anthropic:
    if not os.environ.get("ANTHROPIC_API_KEY"):
        print("환경변수 ANTHROPIC_API_KEY가 필요합니다.", file=sys.stderr)
        sys.exit(1)
    return Anthropic()


def call_aria(state: GameState, user_input: str) -> str:
    client = _client()
    case_context = json.dumps(
        {
            "case_id": state.case["case_id"],
            "title": state.case["title"],
            "premise": state.case["premise"],
            "scenes": [{"scene_id": s["scene_id"], "name": s["name"]} for s in state.case["scenes"]],
            "characters": [
                {"character_id": c["character_id"], "name": c["name"], "role": c["role"]}
                for c in state.case["characters"]
            ],
            "evidence_index": [
                {
                    "evidence_id": e["evidence_id"],
                    "name": e["name"],
                    "discoverable_at": e["discoverable_at"],
                    "discovery_hints": e.get("discovery_hints", []),
                }
                for e in state.case["evidence"]
            ],
            "discovered_evidence": list(state.discovered_evidence),
            "deduction_endings": list(state.case["deduction"]["endings"].keys()),
        },
        ensure_ascii=False,
        indent=2,
    )

    system = (
        ARIA_PROMPT
        + "\n\n## 현재 사건 컨텍스트\n```json\n"
        + case_context
        + "\n```\n\n## 발견 가능한 단서의 전체 묘사\n"
        + json.dumps(
            [
                {"evidence_id": e["evidence_id"], "description": e["description"]}
                for e in state.case["evidence"]
            ],
            ensure_ascii=False,
            indent=2,
        )
    )

    state.aria_history.append({"role": "user", "content": user_input})
    msg = client.messages.create(
        model=GM_MODEL,
        max_tokens=600,
        system=system,
        messages=state.aria_history,
    )
    response_text = "".join(b.text for b in msg.content if hasattr(b, "text"))
    state.aria_history.append({"role": "assistant", "content": response_text})
    return response_text


def call_npc(state: GameState, character_id: str, user_input: str) -> str:
    client = _client()
    character = next(c for c in state.case["characters"] if c["character_id"] == character_id)
    system = render_character_prompt(character)

    # 이미 발견된 단서를 시스템에 알려서 거짓말 게이트가 동작하도록
    discovered = [
        e for e in state.case["evidence"] if e["evidence_id"] in state.discovered_evidence
    ]
    if discovered:
        system += "\n\n## 플레이어가 이미 알고 있는 단서들\n"
        system += "\n".join(f"- {e['name']}: {e['description']}" for e in discovered)
        system += "\n\n위 단서가 당신의 거짓말 영역과 겹치면, 플레이어가 그것을 정확히 제시할 때 거짓말이 무너질 준비를 하라."

    history = state.interrogation_history.setdefault(character_id, [])
    history.append({"role": "user", "content": user_input})
    msg = client.messages.create(
        model=NPC_MODEL,
        max_tokens=350,
        system=system,
        messages=history,
    )
    response_text = "".join(b.text for b in msg.content if hasattr(b, "text"))
    history.append({"role": "assistant", "content": response_text})

    # 메타 토큰 파싱
    m = re.search(r"<<META:anxiety=(\d+),\s*breaking=(true|false),\s*ended=(true|false)>>", response_text)
    if m:
        state.npc_anxiety[character_id] = int(m.group(1))

    return response_text


# ----- Action parsing ------------------------------------------------------

ACTION_RE = re.compile(r"<<ACTION:(\w+)>>")
INTERROGATE_RE = re.compile(r"<<INTERROGATE:(\w+)>>")
ENDING_RE = re.compile(r"<<ENDING:(\w+)>>")
EVIDENCE_TOKEN_RE = re.compile(r"\[찰칵\]|\[띵\]")


def detect_evidence_discovery(state: GameState, aria_text: str) -> list[str]:
    """Aria 응답에서 단서 발견을 휴리스틱으로 감지.
    프로토타입에선 단서명이 직접 등장하면 발견된 것으로 간주."""
    newly_found = []
    for ev in state.case["evidence"]:
        if ev["evidence_id"] in state.discovered_evidence:
            continue
        if ev["name"] in aria_text:
            state.discovered_evidence.add(ev["evidence_id"])
            newly_found.append(ev["evidence_id"])
    return newly_found


# ----- REPL ----------------------------------------------------------------

BANNER = """
============================================================
   Detective Voice — Phase 0 Prototype
   사건: {title}
============================================================
명령:
  > [자유 입력]                — Aria에게 말 걸기
  /talk <character_id>        — NPC 심문 모드 진입
  /done                       — NPC 심문 종료
  /notes                      — 사건 노트 (발견된 단서) 출력
  /accuse                     — 추리 단계로 이동
  /state                      — 디버그 상태
  /quit                       — 종료
"""


def repl(case_path: str) -> None:
    state = GameState.load(Path(case_path))
    print(BANNER.format(title=state.case["title"]))

    # 첫 발화: Aria의 사건 브리핑
    opening = call_aria(state, "(게임 시작. 사건을 브리핑해주세요.)")
    print(f"\n[Aria]\n{opening}\n")

    interrogating: str | None = None

    while not state.ended:
        try:
            prompt = f"({state.case['characters'][[i for i, c in enumerate(state.case['characters']) if c['character_id'] == interrogating][0]]['name']} 심문 중)" if interrogating else "탐정"
        except (StopIteration, IndexError):
            prompt = "탐정"
        try:
            user_input = input(f"\n{prompt}> ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\n게임 종료.")
            break

        if not user_input:
            continue

        if user_input == "/quit":
            break

        if user_input == "/state":
            print(f"\n발견 단서: {sorted(state.discovered_evidence)}")
            print(f"NPC 불안: {state.npc_anxiety}")
            print(f"심문 중: {interrogating}")
            continue

        if user_input == "/notes":
            print(f"\n[사건 노트]\n{state.evidence_summary()}\n")
            continue

        if user_input == "/done":
            interrogating = None
            print("(심문 종료. Aria로 복귀.)")
            continue

        if user_input.startswith("/talk "):
            target = user_input.split(" ", 1)[1].strip()
            if any(c["character_id"] == target for c in state.case["characters"]):
                interrogating = target
                print(f"({target} 심문 모드. /done 으로 빠져나옴.)")
            else:
                print("그런 인물 없음. characters: " + ", ".join(c["character_id"] for c in state.case["characters"]))
            continue

        if user_input == "/accuse":
            print("\n[추리 단계 진입] 범인이 누구이고, 동기와 핵심 증거가 무엇인지 한 문단으로 말해주세요.")
            try:
                deduction = input("\n탐정 (추리)> ").strip()
            except (EOFError, KeyboardInterrupt):
                break
            verdict = call_aria(state, f"(ACCUSE 단계) 플레이어의 추리: {deduction}")
            print(f"\n[Aria]\n{verdict}\n")
            if ENDING_RE.search(verdict):
                state.ended = True
            continue

        # 자유 입력 처리
        if interrogating:
            response = call_npc(state, interrogating, user_input)
            character = next(c for c in state.case["characters"] if c["character_id"] == interrogating)
            print(f"\n[{character['name']}]\n{response}\n")
            anxiety = state.npc_anxiety.get(interrogating, 0)
            print(f"  (불안 미터: {anxiety}/100)")
        else:
            response = call_aria(state, user_input)
            print(f"\n[Aria]\n{response}\n")

            # INTERROGATE 위임 감지
            m = INTERROGATE_RE.search(response)
            if m:
                interrogating = m.group(1)
                print(f"(자동으로 {interrogating} 심문 모드 진입)")

            # 단서 발견 감지
            new_ev = detect_evidence_discovery(state, response)
            if new_ev:
                names = ", ".join(
                    next(e["name"] for e in state.case["evidence"] if e["evidence_id"] == eid)
                    for eid in new_ev
                )
                print(f"  (단서 추가: {names})")

            # 결말 감지
            if ENDING_RE.search(response):
                state.ended = True

    print("\n=== 종료 ===")
    print(f"최종 발견 단서: {len(state.discovered_evidence)}/{len(state.case['evidence'])}")
    print(f"방문 NPC: {len(state.interrogation_history)}/{len([c for c in state.case['characters'] if c['role'] != 'victim'])}")


def main() -> None:
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)
    repl(sys.argv[1])


if __name__ == "__main__":
    main()
