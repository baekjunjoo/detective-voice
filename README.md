# Detective Voice — Phase 0 Prototype

> Dot의 음성 추리 어드벤처 GDD를 검증하기 위한 텍스트 기반 코어 루프 프로토타입.
> 음성 없이 **AI 일관성·거짓말 게이트·풀 수 있는 미스터리** 세 가지를 먼저 본다.

## 디렉토리

```
detective-voice-prototype/
├── PROTOTYPE_ROADMAP.md          ← 4~6주 단계별 계획
├── README.md                     ← 지금 이 파일
├── detective_voice.py            ← 실행 가능한 CLI 게임
├── schemas/
│   └── case_template.schema.json ← 사건 템플릿 JSON 스키마
├── cases/
│   └── last_customer.json        ← 시그니처 사건 1편 풀 템플릿
└── prompts/
    ├── aria_gm.md                ← Aria 게임 마스터 시스템 프롬프트
    └── character.md              ← NPC 캐릭터 시스템 프롬프트 템플릿
```

## 빠른 실행

```bash
cd "/Users/joobaekjun/Documents/Claude/Projects/Dot Arcade/detective-voice-prototype"

# 1) anthropic SDK 설치 (한 번만)
pip install anthropic

# 2) API 키 (console.anthropic.com에서 발급)
export ANTHROPIC_API_KEY="sk-ant-..."

# 3) 게임 시작
python detective_voice.py cases/last_customer.json
```

첫 실행에서 Aria가 사건을 브리핑하면, 자유 입력으로 게임이 진행돼.

### 명령어
| 입력 | 효과 |
|---|---|
| `(자유 한국어)` | Aria에게 말 걸기 / 장면 탐색 / 단서 제시 |
| `/talk park_junyoung` | NPC 심문 모드 진입 |
| `/done` | 심문 종료, Aria로 복귀 |
| `/notes` | 발견된 단서 목록 |
| `/accuse` | 추리·고발 단계로 이동 |
| `/state` | 디버그 (단서·NPC 불안 미터) |
| `/quit` | 종료 |

### 등장 인물 (`/talk <id>`)
- `park_junyoung` — 박준영 (절친, 빚 3천만원)
- `kim_yujin` — 김유진 (박준영의 아내)
- `lee_minji` — 이민지 (와인바 직원)
- `choi_dongsoo` — 최동수 (단골 손님)

## 첫 플레이에서 확인할 5가지

이 프로토타입은 단순 데모가 아니라 **3가지 가설을 검증하는 실험**이다. 1~2회 플레이하면서 다음 5가지를 직접 적어둬.

### 1. 환각 발생률
- Aria나 NPC가 **사건 템플릿(`cases/last_customer.json`)에 없는 사실**을 만들어내는가?
- 예: 존재하지 않는 인물·증거·과거 이력.
- 목표: 사건당 0~1회.

### 2. 거짓말 일관성
- `/talk park_junyoung` 들어가서 다음 3가지를 다른 방식으로 물어봐:
  - "어젯밤 어디 있었어요?"
  - "집에서 뭐 했어요?"
  - "아내랑 같이 있었던 거 맞아요?"
- 박준영은 *항상* "아내랑 영화 '기생충' 봤다"는 거짓말을 유지해야 함.
- 답변이 흔들리면 → H2 깨진 것. 프롬프트 수정 필요.

### 3. 거짓말 무너짐
- 김유진을 먼저 만나서 "남편이 영화 본 적 없다"는 증언을 확보 (`ev_wife_testimony` 발견).
- 그 다음 박준영에게 그 증언을 들이밀어:
  - "당신 아내는 영화 본 적 없다고 하던데요"
- 박준영의 거짓말이 무너지는가? (변명 1~2회 후 침묵 또는 인정)
- 무너지지 않으면 → 거짓말 게이트가 작동 안 한 것.

### 4. 풀 수 있는 난이도
- 끝까지 플레이해서 `/accuse` 실행.
- "박준영이 범인, 동기는 아내와 정민호의 관계, 핵심 증거는 영수증·재고 장부·휴대폰 메시지" — 이렇게 풀 수 있어야 정상.
- `perfect` 결말이 나오는가? `wrong_suspect`나 `inconclusive`면 게임이 너무 어렵거나 단서 묘사가 부족한 것.

### 5. 페이싱 (시간)
- 한 사건 완주에 몇 분 걸렸는가?
- 목표: 35~50분.
- 너무 짧다 → 단서·NPC가 부족. 너무 길다 → Aria가 묘사를 길게 하거나 막힘이 잦음.

## 알려진 한계 (Phase 0 의도적 단순화)

- **단서 발견 휴리스틱**: Aria 응답에 단서 이름이 들어가면 발견 처리. 정밀하지 않음. Phase 1에선 LLM이 직접 `<<EVIDENCE_FOUND:id>>` 토큰을 출력하도록 개선.
- **추리 평가**: Aria(Sonnet)가 자유 응답에서 결말을 결정. 객관성을 높이려면 별도 평가 LLM 또는 룰 기반으로 분리.
- **음성 없음**: STT/TTS 미통합. Phase 1에서 ElevenLabs 스트리밍 + Web Speech 추가.
- **단일 사건**: procedural 사건 생성기 미포함. Phase 1~2에서 Story Engine 호출 추가.
- **Aria 톤**: 시스템 프롬프트만으로 "K-드라마 30대 따뜻한 톤"을 텍스트로 흉내. 진짜 톤은 TTS 보이스 캐스팅에서 결정.

## API 비용 가드

- 1 풀 플레이스루 추정: $0.50~$1.50 (Sonnet GM + Haiku 캐릭터)
- 50회 검증해도 $75 미만
- 비용이 튀면 `GM_MODEL`을 `claude-haiku-4-5`로 다운그레이드해서 단축 검증 가능 (단, 일관성 떨어질 수 있음)

## 다음 단계

이 프로토타입을 5번 풀 플레이스루 한 후:
1. 위 5가지 검증 결과 기록
2. 실패한 항목에 대해 사건 템플릿 또는 프롬프트 수정
3. `PROTOTYPE_ROADMAP.md`의 Phase 1 (웹 음성)으로 진행

**Phase 0이 견고히 통과해야 Phase 1을 시작한다.** AI 코어가 무너지면 음성을 얹어도 게임이 부서진다.

---

## 참고: GDD와의 매핑

| GDD 항목 | 이 프로토타입에서 |
|---|---|
| Layer 1 — Story Engine | `cases/last_customer.json` (수동 작성, M3에 자동 생성기 추가) |
| Layer 2 — Character LLM | `prompts/character.md` + Haiku 4.5 호출 |
| Layer 3 — Game Master Aria | `prompts/aria_gm.md` + Sonnet 4.6 호출 |
| Layer 4 — TTS/STT | Phase 1에서 추가 |
| 단일 진실 소스 | 케이스 JSON을 시스템 프롬프트에 임베드 |
| 거짓말 게이트 | `character.md`의 "거짓말하는 것" 섹션 + breaks_at 트리거 |
| 추리 평가 4분기 | Aria의 `<<ENDING:perfect/conviction/wrong_suspect/inconclusive>>` 토큰 |
| 자유로운 음성 입력 | 텍스트 입력으로 대체. 의미상 동일. |
