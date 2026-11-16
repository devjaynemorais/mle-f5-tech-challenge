.PHONY: install lint format test train drift-simulate drift-report api up down

PY ?= python

install:
	$(PY) -m pip install -r requirements-dev.txt

lint:
	ruff check src tests
	ruff format --check src tests

format:
	ruff check --fix src tests
	ruff format src tests

test:
	pytest

# Etapa 1: treino + tracking (suba antes: docker compose up mlflow)
train:
	$(PY) -m src.classifier.train

# Etapa 3: simulacao de drift + relatorio Evidently
drift-simulate:
	$(PY) -m src.drift.simulate
drift-report:
	$(PY) -m src.drift.report

api:
	uvicorn src.api.main:app --reload --port 8000

up:
	docker compose up --build
down:
	docker compose down
