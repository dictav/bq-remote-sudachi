FROM python:3.12-slim

RUN pip install uv gunicorn

WORKDIR /app
COPY pyproject.toml ./
COPY requirements.lock ./
RUN uv pip install --no-cache --system -r requirements.lock

COPY src .

ENV NUM_WORKER=5
ENV PORT=8000

CMD ["sh", "-c", "gunicorn -w $NUM_WORKER -b 0.0.0.0:$PORT main:app"]
