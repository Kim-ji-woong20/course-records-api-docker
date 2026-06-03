# Course Records API

FastAPI를 이용한 JSON 파일 기반 수강기록 관리 API입니다.

## 기능

- GET `/courses`: 전체 수강기록 조회
- POST `/courses`: 새 수강기록 추가
- `courses.json` 파일 기반 데이터 저장

## 실행 방법

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --reload