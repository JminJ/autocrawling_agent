FROM python:3.10.12-slim-bullseye

# 시스템 패키지 업데이트 및 필요한 패키지 설치
RUN apt update -y && apt upgrade -y

RUN apt-get install -y curl

# 작업 디렉토리 설정
WORKDIR /workspace

# screenshots 디렉토리 생성
RUN mkdir screenshots

# Poetry 설치
RUN pip install poetry==1.8.2

# Poetry 가상 환경 생성 비활성화
RUN poetry config virtualenvs.create false

# `pyproject.toml`과 `poetry.lock` 파일을 컨테이너에 복사
COPY pyproject.toml poetry.lock /workspace

# Poetry를 사용하여 의존성 설치
RUN poetry install

# playwright 설치
RUN playwright install-deps

# 애플리케이션 코드 복사
COPY . /workspace

# 애플리케이션 포트 노출
EXPOSE 8000