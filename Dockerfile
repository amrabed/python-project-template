FROM python:3.14-alpine
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/
WORKDIR /code
COPY . .
RUN uv sync
ENTRYPOINT ["uv", "run", "app"]
