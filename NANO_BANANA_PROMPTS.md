# Nano Banana — Detective Voice 픽셀 아트 프롬프트 세트

> Gemini 2.5 Flash Image용. 14장 시리즈가 같은 톤으로 나오도록 설계.

## 사용법

1. **STYLE_BASE를 매번 프롬프트 앞에 그대로 붙여넣기** — 시리즈 일관성의 핵심.
2. 마음에 드는 첫 이미지가 나오면 → **그 이미지를 다음 프롬프트에 reference로 첨부** → "use this exact style and palette" 추가.
3. 한 번에 4~6장 변형(variation) 만들어보고 가장 좋은 거 선택.
4. 모든 이미지: **4:3 비율** (또는 NPC는 1:1, 단서는 5:3).

---

## STYLE_BASE (모든 프롬프트 앞에 붙임)

```
1-bit black and white pixel art illustration. Pure monochrome palette: 
deep black background, off-white foreground (#f4f1e8), and minimal warm 
amber accent (#f4b54a) used sparingly for highlights only. Heavy halftone 
dot dithering for tonal transitions. 80s retro Macintosh / early computer 
aesthetic with strong line work, crosshatching, and dense pixel detail. 
Influences: Daisuke Ichiba illustration, Susumu Hirasawa album art, 
early Japanese manga panels, Patrick Kyle pixel work, World of Horror 
game art. Sharp pixel edges, no anti-aliasing, no smooth gradients — 
all shading via dithering patterns. Single-panel composition. Noir 
mystery atmosphere. Korean cultural setting where relevant.
```

---

## 시리즈 1 — 장면 (4:3 비율)

### ① 스플래시 / 타이틀 카드

```
[STYLE_BASE]

A vintage 1980s CRT television sitting on a wooden stand, screen 
displaying an audio waveform with 15 vertical bars of varying heights 
in pure white against deep black. Two long antennas extending up with 
small diamond tips. Detailed speaker grills on the right side of the 
TV with 8-10 horizontal slits. Two circular dials below the speakers 
with tick marks and pointer indicators. Small amber LED light glowing. 
The TV is the centerpiece, dramatically lit. Background: pure black 
void with subtle dithered shadow under the stand. Sense of late-night 
detective work, voice being broadcast through the night. No text. 
4:3 aspect ratio. Compose as a striking title card.
```

### ② 와인바 사건 현장 (Crime Scene)

```
[STYLE_BASE]

Interior of a small Korean wine bar named "LUNA" in Gangnam at night. 
Dark wood-tone interior. A wall of wine bottles in shelving across the 
back wall — at least 30 bottles in two rows, with ONE conspicuously 
empty slot in the middle. A long bar counter in the foreground with 
a POS register, a wine glass, an open receipt printed out. Pendant 
lamp hanging from ceiling casting a cone of amber light. On the floor 
behind the counter: a man's silhouette (the victim, in formal shirt) 
lying face-down. A broken wine bottle with shattered glass shards near 
his head, dried blood pool dithered in amber. Yellow police line tape 
("DO NOT CROSS · POLICE LINE") stretching across the upper portion of 
the scene. Three bar stools, one knocked over. Herringbone wood floor. 
"LUNA" sign mounted on the wall in amber. Heavy halftone shading for 
shadows. Cinematic noir composition. 4:3 aspect ratio.
```

### ③ 가게 앞 골목 (Alley)

```
[STYLE_BASE]

A narrow Korean alley at midnight, rain falling. On the left: a 4-story 
brick apartment building with 12 windows, most dark, 2 lit warmly in 
amber. On the right: a 24-hour convenience store with a glowing amber 
"24H" sign, large glass storefront showing shelf silhouettes inside, 
sliding glass door, a small CCTV camera mounted at the corner. In the 
center: a tall street lamp casting a cone of amber light onto the wet 
pavement. Diagonal rain streaks across the entire scene, with the rain 
inside the lamp's light glowing amber. A puddle reflecting the lamp. 
Empty road with faint sidewalk dividers. Slightly desolate, mysterious 
mood. Heavy dithering for atmosphere. 4:3 aspect ratio.
```

### ④ 국과수 부검실 (Morgue)

```
[STYLE_BASE]

Sterile forensic autopsy room, viewed from foot of examination table. 
Long flat metal examination table running across the middle of the 
frame, with a body covered by a clean white sheet — feet visible at 
the near end with a paper toe-tag reading "JM-48", head outline at the 
far end. Sheet has subtle wrinkles and folds rendered in halftone. 
Overhead fluorescent ceiling light casting a downward cone of cold 
amber light. Tile-grid walls in the background. To the left: a 
clipboard with handwritten autopsy chart pinned on the wall. To the 
right: a rack of stainless steel surgical instruments on a wall mount, 
and a small X-ray light box showing a human silhouette with a red X 
mark on the back of the skull. Drain on the polished floor in 
foreground. Clinical, eerie atmosphere. 4:3 aspect ratio.
```

---

## 시리즈 2 — 단서 (5:3 비율, 클로즈업)

### ⑤ 깨진 와인병 (Broken Bottle)

```
[STYLE_BASE]

Extreme close-up of a broken wine bottle lying horizontally on a 
concrete floor. The bottle is shattered at the base end, with jagged 
glass shards radiating outward. The label is half-torn off, but visible 
text reads "CHÂTEAU MARGAUX 2015" in elegant amber serif type on a 
black label background. Glass body in white, broken jagged edge in 
detailed zigzag pattern. Dried blood smeared near the broken end, 
rendered in amber halftone dithering. Several scattered glass fragments 
around the bottle, some catching amber highlights. Forensic evidence 
marker "EVIDENCE 01" tag in amber at top-left corner. Measurement 
ruler (20 CM) along the bottom. Composition feels like a CSI evidence 
photo. 5:3 aspect ratio.
```

### ⑥ POS 영수증 (Receipt 23:42)

```
[STYLE_BASE]

A long thermal-printed receipt from a Korean wine bar named "LUNA 
WINEBAR · SEOUL", floating against a black void, slightly angled. 
Receipt paper is off-white with sharp zigzag torn edges top and bottom. 
Printed content in monospace black text includes: large "LUNA" logo 
header, order number "N-2026-0058", date "2026-05-07", TIME field 
highlighted with amber background showing "23:42:18" in bold, cashier 
"JEONG M.H.", a single line item "CHÂTEAU MARGAUX 2015 / 1 BTL · 
350,000 KRW", VAT, total "385,000 KRW" in big bold, card "****-****
-1284", and cardholder "PARK J.Y." highlighted in amber. "APPROVED" 
stamp at bottom. Tag at corner reads "EVIDENCE 02" in amber. The 
"23:42" timestamp has an amber arrow pointing to it labeled "CRITICAL". 
5:3 aspect ratio.
```

### ⑦ 휴대폰 메시지 (Text Message)

```
[STYLE_BASE]

A modern smartphone (iPhone-style with notch) held in portrait 
orientation against a black void. The phone screen displays a Korean 
text message conversation with sender "김유진" (Kim Yu-jin). Status 
bar at top showing signal/wifi/battery icons in pixel art style. 
Header has a small circular avatar in amber. Three message bubbles 
visible: incoming gray bubble "오늘 가게 들를 수 있어?", outgoing 
amber bubble "8시 이후엔 들어와도 돼", incoming gray bubble "알았어. 
보고 싶었어". Then a date divider "— 3일 전 —". Then a large 
highlighted bubble bordered in amber containing the smoking gun 
message: "준영이가 눈치챈 것 같아. 어제 핸드폰 한참 보더라. 우리 
정리하자." with "우리 정리하자." in bold amber. Bottom shows iOS 
keyboard input bar. Amber arrow labeled "SMOKING GUN" pointing to the 
final message. "EVIDENCE 03" tag in amber at corner. 5:3 aspect ratio.
```

### ⑧ 재고 장부 (Wine Inventory Notebook)

```
[STYLE_BASE]

A handwritten Korean notebook page lying flat, slightly angled, against 
a black wood-grain background. The page is off-white with horizontal 
blue ruled lines and a red left margin. Three punch-holes on the left 
edge. Title at top in cursive Korean handwriting: "5월 7일 — 와인 
재고" with the wine bar owner's name "정민호" in italic. Below: a 
handwritten list of wine inventory:
- Châteauneuf 2018 ········ 4병
- Bordeaux 2017 ··········· 6병  
- Pinot Noir 2020 ········· 9병
Then a CRITICAL line highlighted with amber background: 
"Château Margaux 2015 ···· 0병" with a big red "X" mark over the 
quantity. Two cursive notes below in red ink:
- "→ 21:00 최동수 단골 마지막 1병"
- "→ 다음주 화요일 입고 예정"
More wine entries follow. Bottom of page has a small fingerprint 
smudge. Page corner shows "p.42". "EVIDENCE 04" amber tag at top-left. 
5:3 aspect ratio.
```

### ⑨ 편의점 CCTV (CCTV Footage)

```
[STYLE_BASE]

A grainy CCTV surveillance monitor view, rendered as if seen through 
a CRT screen. White rectangular monitor frame with deep black bezel. 
Inside the screen: a low-angle nighttime view of a Seoul alley with 
a wine bar entrance labeled "LUNA" in amber center, brick apartment 
building on the left, another building on the right. A single male 
silhouette (suspect) in dark clothing is captured exiting the wine 
bar, halfway through the doorway, with a long shadow cast by an amber 
street lamp. Bold red CCTV overlay: top-left "CAM-03 GS25 GANGNAM", 
top-right "● REC" in flashing red, top-center timestamp "2026-05-08 
00:15:42" in amber. Red arrow pointing to suspect labeled in red 
"SUSPECT 22:10 → 00:15  +45 MIN". Heavy CRT scanlines across the 
entire frame. Bottom shows monitor footer "SIGNAL: STRONG · PLAYBACK 
1x · HDD 84%". "EVIDENCE 05" amber tag at corner. 5:3 aspect ratio.
```

### ⑩ 부검 보고서 (Autopsy Report)

```
[STYLE_BASE]

A clinical autopsy report clipped to a metal clipboard, viewed straight 
on against a dark background. Off-white paper with crisp printed text. 
Black header bar reads "AUTOPSY REPORT" in bold uppercase, subtitle 
"NATIONAL FORENSIC SERVICE · ROK" in amber. Below the header are typed 
data lines in monospace font:
- CASE #: 2026-0507-LUNA-001
- VICTIM: JEONG MIN-HO (M, 48)
- DATE: 2026-05-07
- EXAMINER: DR. KIM SOO-YEON
Then two CRITICAL fields each highlighted with amber background:
- CAUSE OF DEATH: "BLUNT FORCE TRAUMA — POSTERIOR CRANIUM"
- TIME OF DEATH: "23:30 — 23:45 (ESTIMATED)"
On the right side: a simple line-drawing of a human body diagram in 
black outline, with a red circle and X mark on the back of the head 
labeled "IMPACT" in red. A diagonal red rubber stamp at the bottom 
right reads "CONFIRMED · 2026.05.07 14:22". Handwritten cursive 
doctor's signature in lower-left "Dr. K. S-Y". "EVIDENCE 06" amber 
tag at top-left. 5:3 aspect ratio.
```

---

## 시리즈 3 — NPC 인물 (1:1 비율, 어깨까지)

### ⑪ 박준영 — 용의자, 절친

```
[STYLE_BASE]

Detailed pixel art portrait of a 45-year-old Korean man named Park 
Jun-young. Black formal business suit with a dark amber tie. White 
collared shirt visible at the V-neck. Black hair combed neatly with 
a side part, slightly graying at temples. Face shape: angular, 
guarded. Eyes are narrow and tense, almost squinting. Eyebrows slightly 
furrowed. Closed thin lips pressed together. Subtle stubble shadow on 
jaw. Looking slightly off-camera, the look of someone trying to hide 
something. Atmospheric lighting from the left, deep halftone shadow on 
the right side of the face. Plain dark background. Mugshot composition 
but more dignified. 1:1 aspect ratio. Strong line work for facial 
features. Pure 1-bit B&W with amber tie accent only.
```

### ⑫ 김유진 — 피해자의 비밀 연인

```
[STYLE_BASE]

Detailed pixel art portrait of a 42-year-old Korean woman named Kim 
Yu-jin. Soft cream-colored blouse with subtle dithered texture. Long 
straight black hair falling past her shoulders, with neat bangs across 
the forehead. Small amber earrings visible at the ears. A delicate 
amber necklace at her collarbone. Face shape: gentle, soft. Eyes are 
downturned and sad, with subtle tear tracks rendered in amber. 
Eyebrows slightly raised in melancholy. Lips slightly parted, trembling 
quality. Looking down at an unseen object. Halftone shading captures 
her grief. Plain pale background with subtle dithering. 1:1 aspect 
ratio. Composition feels like a moment of private mourning.
```

### ⑬ 이민지 — 와인바 직원

```
[STYLE_BASE]

Detailed pixel art portrait of a 29-year-old Korean woman named Lee 
Min-ji. White button-up shirt under an amber apron tied with thick 
black straps. The apron has a chest pocket. A small amber name tag 
reads "민지". Black hair pulled back into a ponytail held by an amber 
band, with neat bangs across her forehead. Face shape: round, youthful. 
Large round bright eyes with visible pupils, conveying alertness. Light 
blush dithered on cheeks in amber. A small genuine smile turning up at 
the corners. Slight scattered freckles. Energetic, friendly demeanor. 
Plain bright background. 1:1 aspect ratio. Approachable and confident 
expression.
```

### ⑭ 최동수 — 단골 손님

```
[STYLE_BASE]

Detailed pixel art portrait of a 55-year-old Korean man named Choi 
Dong-soo. Wearing a baseball cap with an amber band around the middle 
and a white "B" logo on the front. Casual plaid shirt with subtle 
checkered pattern. Salt-and-pepper hair visible at the temples. 
Friendly weathered face with soft round cheeks, light age spots, and 
laugh lines around eyes. Eyes are crinkled and smiling — drawn as 
curved upward arcs, the classic "smile eyes" expression. Bushy eyebrows. 
Thick salt-and-pepper mustache. Wide warm grin showing a hint of 
upper teeth. Looks like someone's favorite uncle. Casual neighborhood 
regular vibe. Plain background. 1:1 aspect ratio. Warm and 
approachable expression.
```

---

## 사용 팁

### 일관성 확보

1. **첫 이미지(추천: 스플래시 또는 와인바)를 가장 정성껏 만들어**. 만족스러운 결과 나올 때까지 10~20회 변형 돌려.
2. 그 이미지를 다음 프롬프트에 첨부 + `"Use this exact pixel art style, halftone density, line weight, and color palette as visual reference for this new scene."` 추가.
3. 14장 다 끝났을 때 마음에 안 드는 게 있으면 그 한 장만 다시 → 이미 만들어둔 만족스러운 이미지를 reference로 첨부.

### 디테일 조정 키워드

품질이 부족하면 프롬프트에 추가:
- `"hand-drawn pixel art quality, every pixel placed deliberately"`
- `"reminiscent of Aseprite artwork by professional pixel artists"`
- `"newspaper print style halftone, dot screen"`
- `"density similar to early Macintosh hypercard games"`

너무 어지러우면:
- `"clean composition, breathing room around subject"`
- `"high contrast, simplified shapes"`

### Aspect Ratio 명시법

나노바나나에서 잘 동작하는 비율 지정:
- 장면: `4:3 aspect ratio` 또는 `1024x768` 명시
- 단서: `5:3 aspect ratio` 또는 `1024x600`
- NPC: `1:1 aspect ratio` 또는 `768x768`

### 한국어 텍스트가 깨질 때

나노바나나는 한국어 텍스트를 종종 변형/오타 발생시켜. 그럴 땐:
1. 한국어 텍스트를 영문으로 바꿔서 일단 생성 (예: "준영이가 눈치챈 것" → "He noticed it")
2. 또는 텍스트 부분만 비워두라고 명시: `"leave text area blank for later overlay"`
3. 한국어 텍스트가 들어가야 할 자리만 Figma/포토샵에서 후작업으로 한국어 입력

---

## 통합 — 생성된 이미지를 데모에 박는 법

이미지가 마음에 들게 나오면:

1. **저장**: PNG 또는 JPG로 저장, 파일명을 명확하게 (예: `splash.png`, `wine_bar.png`, `ev_receipt.png`)
2. **폴더 생성**: `detective-voice-prototype/img/` 폴더 만들고 14장 다 넣기
3. **나에게 보내줘**: 이미지 14장 다 준비되면 알려줘. SVG 자리를 `<img>` 태그로 교체하는 코드는 내가 30분 안에 짜줄게.

또는 — 단순히 v5 SVG 위에 이미지를 한 장 한 장 갈아끼우면서 점진적으로 업그레이드해도 돼. 가장 인상 깊은 한 장(예: 스플래시)부터 시작.

---

## 예산 / 시간 예상

- **나노바나나 비용**: Google AI Studio에서 무료 등급 사용 가능 (월 일정 수량). 또는 API 키로 더 많이 — 이미지 1장당 약 $0.04 USD.
- **14장 작업 시간**: 한 장당 10~20회 변형 돌리면 평균 30분. 전체 약 5~8시간 (마음에 들 때까지).
- **전체 비용**: $10 미만 (무료 등급 안에서) ~ $30 (변형 많이 돌릴 경우).

투자자/인터뷰 데모 비주얼을 결국 하루 작업으로 끝낼 수 있다는 얘기야. 픽셀 아티스트 외주 ₩50~200만원과 비교하면 압도적으로 싸고 빨라.

---

## 한 가지 주의

나노바나나가 폭력 묘사(시신, 혈흔 등)에 대해 안전 필터를 걸 수 있어. 그럴 땐 표현 완화:
- "victim's body" → "covered figure" 또는 "silhouette of a person"
- "blood pool" → "dark stain" 또는 "amber spill"
- "broken bottle with blood" → "scattered glass shards near a dark mark"

부검실/사건 현장이 막히면 이런 식으로 우회해서 분위기만 만들고, 결정적 디테일은 후작업으로 추가.
