# Backend API

## 폴더 구성
```bash
.
    └── app/
        ├── api/
        │   ├── music/
        │   │   ├── controller.py: API endpoint
        │   │   ├── schemas.py: Type model, enum
        │   │   ├── services.py: API에서 사용하는 method
        │   │   └── validation.py: Validate request parameter
        │   └── router.py
        ├── main.py
        ├── settings.py: 환경변수
        └── README.md
```

## Install

1. Install python environment (pyenv, virtualenv, ...)
2. Install poetry, fastapi, uvicorn
```shell
$ pip(pip3) install poetry fastapi uvicorn
```
3. Install packages
```shell
$ poetry install
```

## 서버 실행 방법

1. app folder로 이동
```shell
$ cd app
```
2. 서버 실행
```shell
app$ uvicorn main:app --reload
```
3. Swagger UI URL
```shell
http://localhost:8000/docs
```