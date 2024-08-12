FROM python:3.11-buster AS builder

RUN pip install poetry~=1.8.3

ENV POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_IN_PROJECT=1 \
    POETRY_VIRTUALENVS_CREATE=1 \
    POETRY_CACHE_DIR=/tmp/poetry_cache

WORKDIR /app

COPY pyproject.toml poetry.lock ./
RUN touch README.md

RUN --mount=type=cache,target=$POETRY_CACHE_DIR
RUN poetry install --without dev --no-root

COPY metealologia_backend ./metealologia_backend
RUN poetry install --only-root

FROM python:3.11-slim-buster AS runtime

WORKDIR /app

ENV VIRTUAL_ENV=/app/.venv
ENV PATH="/app/.venv/bin:$PATH"

ENV HOST=0.0.0.0
ENV PORT=80

COPY --from=builder ${VIRTUAL_ENV} ${VIRTUAL_ENV}

COPY metealologia_backend ./metealologia_backend

EXPOSE ${PORT}

ENTRYPOINT ["python", "-m", "metealologia_backend.main"]
