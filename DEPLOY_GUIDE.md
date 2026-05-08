# 깃헙에 올려서 링크 만들기

> 개발자 아니어도 됨. 클릭만으로 5분.

목표: `https://[당신_이름].github.io/detective-voice/` 같은 공개 URL을 받아서 인터뷰이/투자자/공동창업자 후보에게 그냥 링크만 던지면 되게.

---

## 옵션 A — GitHub Pages (추천, 5분, 영구 URL)

### 1단계: 깃헙 계정 만들기 (이미 있으면 건너뛰기)

[github.com/signup](https://github.com/signup) → 이메일/비밀번호/사용자명 입력.

> **중요**: 사용자명이 URL에 들어가. 회사 명의면 `dot-inc` 같은 식, 개인이면 본인 이름. 한 번 정하면 바꾸기 번거로워.

### 2단계: 새 저장소(Repository) 만들기

1. 우측 상단 `+` 버튼 → `New repository`
2. **Repository name**: `detective-voice` (이게 URL의 마지막 부분이 됨)
3. **Description** (선택): `Voice-based AI mystery game by Dot Inc.`
4. **Public** 선택 (Pages 무료 사용 조건)
5. **Add a README file** 체크
6. `Create repository` 클릭

### 3단계: 파일 업로드

저장소 페이지에서:

1. `Add file` 버튼 → `Upload files`
2. **`detective-voice-prototype` 폴더 안의 모든 파일**을 드래그 앤 드롭 (또는 `choose your files`로 선택)
   - 가장 중요한 파일: **`index.html`** ← 이게 자동으로 홈페이지가 됨
   - 나머지 (`demo.html`, `demo_v2.html` 등)도 같이 올리면 백업 버전으로 접근 가능
3. 화면 아래쪽 `Commit changes` 클릭

### 4단계: GitHub Pages 켜기

저장소 상단 메뉴에서:

1. `Settings` 탭 클릭
2. 왼쪽 사이드바에서 `Pages` 클릭
3. **Source** 섹션에서:
   - `Deploy from a branch` 선택
   - Branch: `main` / 폴더: `/ (root)`
4. `Save` 클릭

### 5단계: URL 확인 (1~3분 기다리기)

같은 `Pages` 페이지를 새로고침하면 위쪽에 이렇게 떠:

> ✅ **Your site is live at https://[당신_이름].github.io/detective-voice/**

이 URL이 영구 공개 링크. 한 번 만들면 평생 안 바뀜. 폰/노트북/태블릿 어디서나 열려.

---

## 옵션 B — Netlify Drop (1분, 계정 불필요, 임시 URL)

빠르게 한 번 보여주는 용도면:

1. [netlify.com/drop](https://app.netlify.com/drop) 접속
2. `detective-voice-prototype` 폴더를 통째로 화면에 드래그
3. 즉시 URL 받음: `https://random-name-abc123.netlify.app/`

**단점**: 24시간 후 사라짐 (계정 없는 경우). 영구 URL 원하면 Netlify 무료 계정 가입 (1분).

---

## 어느 쪽이 좋아?

| 상황 | 추천 |
|---|---|
| 투자자/팀에게 공식 공유 | **GitHub Pages** (URL이 깨끗하고 영구적) |
| 인터뷰 참여자에게 링크 전달 | **GitHub Pages** |
| 30분 후 미팅에서 빠르게 보여주기 | **Netlify Drop** |
| 본인 폰에서 한 번 테스트 | 둘 다 가능 |

---

## 데모 업데이트하는 법 (나중에 사건 추가 등)

수정한 파일을 깃헙 저장소에 다시 올리면 끝:

1. 저장소 페이지에서 `index.html` 클릭
2. 우측의 연필 아이콘 ✏️ → 편집
3. 또는 `Add file` → `Upload files`로 새 파일 드래그
4. `Commit changes`

깃헙 페이지가 1~2분 안에 자동으로 반영함.

---

## 자주 묻는 것

### Q. 코드가 공개되는데 괜찮나?

A. 데모 코드는 어차피 누구나 브라우저에서 "소스 보기"로 볼 수 있어. 영업 비밀 같은 건 없고, 사건 시나리오는 픽션이라 괜찮음. 오히려 "오픈소스로 시각장애 게임 만들고 있다" 같은 스토리텔링이 강해져.

### Q. API 키는 어떻게 되나?

A. 키는 사용자 **본인 브라우저 sessionStorage**에만 저장돼. 깃헙에도, 어디에도 안 올라가. 인터뷰할 때 본인 노트북에서 한 번 키 입력하고, 그 노트북으로 인터뷰이가 굴리면 돼. 인터뷰이가 다른 폰/PC에서 같은 URL 열면 거기엔 키가 없으니 클릭 모드로 동작.

### Q. 사용량 제한은?

A. 깃헙 페이지 무료 등급:
- 월 100GB 트래픽
- 빌드 10분/월
- 데모용으론 무한대로 쓸 수 있음 (월 수만 명 방문해도 안 넘음)

### Q. 도메인을 `detectivevoice.com` 같은 걸로 바꿀 수 있나?

A. 가능. 도메인 사서 (gabia, godaddy 등) DNS에 깃헙 페이지 IP를 가리키게 하면 됨. 비개발자에게 살짝 복잡하니 일단은 깃헙 기본 URL로 시작하고, 나중에 정식 출시 직전에 바꾸면 돼.

### Q. 사용자 트래픽/방문 통계는 볼 수 있나?

A. 깃헙 페이지 자체엔 분석 도구 없음. 필요하면 [Plausible](https://plausible.io) (무료 30일 체험) 또는 Google Analytics를 `index.html`에 한 줄 추가해서 붙일 수 있어. 인터뷰 단계에선 굳이 필요 없음.

---

## 다음 단계

URL 받은 후:

1. **본인이 폰으로 테스트** — 진짜 모바일 환경에서 어떻게 보이는지
2. **인터뷰이 5명에게 링크 보내기** — "이거 한 번 해보시고 30분 통화 가능할까요?"
3. **공동창업자 후보에게 보내기** — "이런 거 만들고 있는데 같이 할래?"
4. **투자자에게 보내기** — 피치덱 마지막 슬라이드에 URL 박아두기

게임이 진화할 때마다 같은 URL은 그대로 살아 있고, 내용만 업데이트돼. 이게 깃헙 페이지의 강점이야.
