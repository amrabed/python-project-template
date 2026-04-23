FROM python:3.12-alpine
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/
WORKDIR /code
RUN apk add -u make
COPY . .
RUN make install
ENTRYPOINT ["uv", "run", "app"]
