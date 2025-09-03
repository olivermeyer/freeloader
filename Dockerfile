FROM python:3.12-bullseye

ENV PYTHONUNBUFFERED=1 \
    POETRY_VERSION=2.0.1 \
    POETRY_VIRTUALENVS_IN_PROJECT=true

WORKDIR /app

RUN pip install --no-cache-dir "poetry==$POETRY_VERSION"

COPY pyproject.toml poetry.lock ./

RUN poetry install --no-interaction	--no-ansi --no-root

COPY src ./src
COPY README.md ./

RUN useradd -m appuser && \
    mkdir -p /app/db_data && \
    chown -R appuser /app
USER appuser
