FROM python:3.10-slim
COPY --from=ghcr.io/astral-sh/uv:0.5.20 /uv /uvx /bin/

COPY  pyproject.toml pyproject.toml
RUN uv pip install --system --no-cache-dir -r pyproject.toml

COPY ./src /app
WORKDIR /app

EXPOSE 5000
CMD ["python3", "app.py"]