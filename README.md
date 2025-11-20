# sample-posts-api

Clean Architecture 기반의 Flask REST API 샘플 프로젝트

## 개요

이 프로젝트는 Clean Architecture 원칙을 따르는 Flask 기반 REST API입니다. Posts와 Comments를 관리하는 간단한 블로그 API를 구현하며, 도메인 주도 설계(DDD)와 의존성 역전 원칙을 적용했습니다.

## 주요 기능

- Posts CRUD 작업
- Comments CRUD 작업
- Swagger UI를 통한 API 문서화
- 메모리/MySQL 저장소 지원
- Docker 기반 배포
- 환경별 설정 관리

## 프로젝트 구조

```
sample-posts-api/
├── app/
│   ├── __init__.py           # Flask 애플리케이션 팩토리
│   ├── config.py             # 환경별 설정
│   ├── extensions.py         # Flask 확장 (CORS, Marshmallow)
│   ├── api/                  # API 엔드포인트
│   │   ├── posts.py          # Posts API
│   │   └── comments.py       # Comments API
│   ├── core/                 # 핵심 비즈니스 로직
│   │   ├── domain/           # 도메인 모델
│   │   │   ├── post.py
│   │   │   └── comment.py
│   │   ├── request_objects/  # 요청 객체
│   │   ├── response_objects/ # 응답 객체
│   │   ├── use_cases/        # 유스케이스 (비즈니스 로직)
│   │   └── base/             # 기본 인터페이스
│   ├── repositories/         # 데이터 저장소
│   │   ├── mem/              # 메모리 저장소
│   │   └── sqla/             # SQLAlchemy 저장소
│   ├── serializers/          # Marshmallow 스키마
│   ├── swagger/              # Swagger 설정
│   └── main/                 # 메인 블루프린트
├── tests/                    # 테스트 코드
├── requirements/             # 환경별 의존성
│   ├── common.txt
│   ├── dev.txt
│   ├── prod.txt
│   ├── test.txt
│   └── docker.txt
├── application.py            # 애플리케이션 진입점
├── Dockerfile                # Docker 이미지 빌드 설정
└── boot.sh                   # Docker 컨테이너 시작 스크립트
```

## Clean Architecture 레이어

### 1. Domain Layer (core/domain/)
- 비즈니스 엔티티 정의
- 외부 의존성 없는 순수한 Python 클래스
- `Post`, `Comment` 도메인 모델

### 2. Use Cases Layer (core/use_cases/)
- 애플리케이션 비즈니스 로직
- Request/Response 객체를 통한 데이터 전달
- Repository 인터페이스에 의존

### 3. Interface Adapters Layer
- **API Layer** (api/): Flask 라우트 및 엔드포인트
- **Repositories** (repositories/): 데이터 저장소 구현
- **Serializers** (serializers/): 데이터 직렬화

### 4. Frameworks & Drivers Layer
- Flask 프레임워크
- SQLAlchemy ORM
- MySQL 데이터베이스

## 기술 스택

- **Framework**: Flask 1.1.1
- **ORM**: SQLAlchemy
- **Database**: MySQL / In-Memory
- **Serialization**: Marshmallow
- **API Documentation**: Flask-Swagger
- **CORS**: Flask-CORS
- **Validation**: Voluptuous
- **Test Data**: Faker
- **WSGI Server**: Gunicorn

## 설치 및 실행

### 로컬 개발 환경

1. 의존성 설치:
```bash
pip install -r requirements/dev.txt
```

2. 환경 변수 설정:
```bash
export FLASK_APP=application.py
export FLASK_CONFIG=development
```

3. 데이터베이스 설정 (MySQL 사용 시):
```bash
# app/config.py에서 REPO_ENGINE = 'MYSQL' 확인
# MySQL 연결 정보 설정
export DEV_DATABASE_URL="mysql+mysqlconnector://user:secret@localhost:3306/posts_api"
```

4. 애플리케이션 실행:
```bash
flask run
```

### Docker 실행

```bash
docker build -t sample-posts-api .
docker run -p 5000:5000 sample-posts-api
```

## API 엔드포인트

### Posts
- `GET /api/v1/posts` - 게시물 목록 조회
- `POST /api/v1/posts` - 새 게시물 생성
- `GET /api/v1/posts/<post_id>` - 특정 게시물 조회
- `PUT /api/v1/posts/<post_id>` - 게시물 수정
- `DELETE /api/v1/posts/<post_id>` - 게시물 삭제

### Comments
- `POST /api/v1/posts/<post_id>/comments` - 댓글 생성

### Swagger 문서
- `/swagger` - Swagger UI

## 환경 설정

프로젝트는 다양한 환경 설정을 지원합니다:

- **development**: 개발 환경 (DEBUG 모드)
- **testing**: 테스트 환경 (SQLite 사용)
- **production**: 프로덕션 환경
- **heroku**: Heroku 배포
- **docker**: Docker 컨테이너
- **unix**: Unix 서버 (syslog 사용)

환경 설정은 `FLASK_CONFIG` 환경 변수로 지정:
```bash
export FLASK_CONFIG=production
```

## 테스트

```bash
# 테스트 의존성 설치
pip install -r requirements/test.txt

# 테스트 실행
pytest tests/
```

## Repository 패턴

프로젝트는 두 가지 저장소 구현을 제공합니다:

1. **메모리 저장소** (repositories/mem/): 빠른 개발 및 테스트용
2. **SQLAlchemy 저장소** (repositories/sqla/): 프로덕션 데이터베이스 사용

`app/config.py`의 `REPO_ENGINE` 설정으로 전환:
```python
REPO_ENGINE = 'MEMORY'  # 또는 'MYSQL'
```

## 라이선스

MIT License
