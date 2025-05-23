FROM python:3.12-slim

RUN apt-get update && apt-get install -y gcc curl libpq-dev python3-dev

RUN curl -sSL https://install.python-poetry.org | python3 -

ENV PATH="/root/.local/bin:$PATH"

WORKDIR /src

COPY pyproject.toml poetry.lock ./
COPY . .

COPY .env .env

RUN poetry install --no-interaction --only main --no-root

EXPOSE 8000

# Запускаємо сервер
CMD ["poetry", "run", "python3", "main.py"]