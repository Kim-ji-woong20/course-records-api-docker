# Course Records API Docker

FastAPI 기반 수강기록 Course Records API를 Docker 컨테이너로 실행하고, AWS Learner Lab EC2 환경에 배포하는 실습 프로젝트입니다.

## 프로젝트 개요

이 프로젝트는 이전 FastAPI 수강기록 API를 Docker 환경에서 실행할 수 있도록 구성한 것입니다.

주요 기능은 다음과 같습니다.

* `GET /courses`: 전체 수강기록 조회
* `POST /courses`: 새로운 수강기록 추가
* `courses.json` 파일 기반 데이터 관리
* Dockerfile을 이용한 이미지 빌드
* docker-compose를 이용한 컨테이너 실행
* EC2 외부 80번 포트를 통한 FastAPI 서비스 접속

## 프로젝트 구조

```text
course-records-api-docker/
├── main.py
├── courses.json
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── README.md
└── .gitignore
```

## 주요 파일 설명

| 파일                   | 설명                              |
| -------------------- | ------------------------------- |
| `main.py`            | FastAPI 서버 실행 코드                |
| `courses.json`       | 수강기록 데이터 저장 파일                  |
| `requirements.txt`   | Python 패키지 의존성 목록               |
| `Dockerfile`         | FastAPI 애플리케이션 Docker 이미지 빌드 설정 |
| `docker-compose.yml` | 컨테이너 실행, 포트 매핑, 재시작 정책 설정       |
| `.gitignore`         | Git에서 제외할 파일 설정                 |

## API 엔드포인트

### GET `/courses`

저장되어 있는 전체 수강기록 리스트를 반환합니다.

```text
GET http://localhost/courses
```

### POST `/courses`

새로운 수강기록을 추가합니다.

```text
POST http://localhost/courses
```

요청 Body 예시:

```json
{
  "course_name": "인간로봇상호작용",
  "year": "2026",
  "semester": "2",
  "grade": "A+"
}
```

## Docker 실행 방법

### 1. Docker 이미지 빌드 및 컨테이너 실행

```bash
docker compose up -d --build
```

### 2. 실행 중인 컨테이너 확인

```bash
docker ps
```

### 3. 브라우저 접속

```text
http://localhost/docs
```

또는

```text
http://localhost/courses
```

## EC2 배포 방식

AWS Learner Lab의 EC2 환경에서 프로젝트를 clone한 뒤 Docker 컨테이너를 실행합니다.

```bash
git clone https://github.com/Kim-ji-woong20/course-records-api-docker.git
cd course-records-api-docker
sudo docker compose up -d --build
```

컨테이너 실행 확인:

```bash
sudo docker ps
```

EC2 보안 그룹에서 80번 포트를 허용한 뒤, 브라우저에서 아래 형식으로 접속합니다.

```text
http://EC2_PUBLIC_IP/docs
```

또는

```text
http://EC2_PUBLIC_IP/courses
```

## Docker Compose 설정

`docker-compose.yml`에서는 외부 80번 포트를 컨테이너 내부 8000번 포트와 연결합니다.

```yaml
ports:
  - "80:8000"
```

또한 컨테이너 자동 재시작 조건을 만족하기 위해 다음 설정을 적용했습니다.

```yaml
restart: always
```

## 실행 조건

* 외부 접속 포트: `80`
* 컨테이너 내부 FastAPI 포트: `8000`
* 재시작 정책: `restart: always`
* 배포 환경: AWS Learner Lab EC2
* Docker Hub 사용: 필수 아님