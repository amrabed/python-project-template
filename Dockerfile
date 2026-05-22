FROM python:3.14-alpine

# Install uv
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# Set environment variables
ENV UV_COMPILE_BYTECODE=1
ENV PATH="/code/.venv/bin:$PATH"

# Set working directory
WORKDIR /code

# Copy project files
COPY . .

# Sync dependencies (frozen and no-dev for production)
RUN uv sync --frozen --no-dev

# Create a non-root user and change ownership
RUN adduser -D appuser && chown -R appuser:appuser /code

# Switch to non-root user
USER appuser

# Run the application directly
ENTRYPOINT ["app"]
