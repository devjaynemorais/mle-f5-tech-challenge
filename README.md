# Copilot de Suporte: Triagem, RAG e Observabilidade

Datathon da Fase 5 (FIAP MLE). O enunciado está em
`docs/MLET - Datathon - Fase 5.pdf`.

Fluxo: um chamado chega à API, um modelo clássico classifica a categoria e o
Evidently monitora drift. Para dúvidas técnicas, o endpoint `/chat` aciona um
RAG sobre manuais em PDF, protegido por guardrails.

> **Status:** estrutura criada; implementação pendente. O **dataset ainda não
> foi escolhido** (a definir pelo time).

## Estrutura

```
config/config.yaml        parâmetros (colunas, chunking, guardrails)
data/raw|processed        dados (fora do Git)
data/manuals/             manuais em PDF usados pelo RAG
src/classifier/           Etapa 1: dados, treino (+MLflow) e inferência
src/api/                  FastAPI: /health, /triage, /chat; schemas Pydantic
src/rag/                  Etapa 2: PDF, chunking, vector store, cadeia LLM
src/guardrails/           Etapa 2: regras de entrada, PII, checagem de saída
src/drift/                Etapa 3: simulação de drift e relatório Evidently
reports/                  relatório HTML do Evidently (entregável)
docs/                     enunciado, checklist, decisões
tests/                    pytest
Dockerfile, docker-compose.yml, requirements.txt   Etapa 4
```

## Execução (alvo)

```bash
cp .env.example .env          # preencher a chave do LLM
make install
docker compose up mlflow -d   # MLflow em http://localhost:5000
make train                    # treino + métricas no MLflow
make drift-simulate drift-report
make api                      # Swagger em http://localhost:8000/docs
```

Ou tudo via Docker: `docker compose up --build`.

## Arquitetura de Nuvem

_A preencher (AWS, Azure ou GCP): como escalar o container da API._

## Privacy by Design (LGPD)

_A preencher: mascaramento de PII em `src/guardrails/pii.py` antes de enviar
texto ao LLM, minimização de dados e logs sem conteúdo sensível._

## Vídeo (5 min, STAR)

_Link a adicionar: API (Swagger/Postman), painel MLflow e relatório de drift._
