# AGENTS.md

Guia para agentes neste repositório: Datathon Fase 5 (FIAP MLE), um "Copilot de
Suporte" com triagem (ML clássico), RAG sobre PDF com guardrails e observabilidade.
Enunciado: `docs/MLET - Datathon - Fase 5.pdf`. Requisitos: `docs/checklist_requisitos_datathon.md`.

## Mapa

- `config/config.yaml`: parâmetros; segredos só no `.env` (nunca commitar).
- `src/classifier/`: dados, treino com MLflow, inferência.
- `src/api/`: FastAPI (`/health`, `/triage`, `/chat`) e schemas Pydantic.
- `src/rag/`: PDF, chunking, vector store, cadeia LLM.
- `src/guardrails/`: entrada, PII (antes do LLM) e saída.
- `src/drift/`: simulação de drift e relatório Evidently em `reports/`.

## Regras

- O dataset ainda não foi escolhido pelo time; não assumir um.
- O `/chat` responde apenas com base no PDF; sem contexto, recusa.
- Nunca enviar PII ao LLM sem passar por `redact_pii`.
- Dados e artefatos treinados ficam fora do Git.
- Comandos: `make install | lint | test | train | drift-simulate | drift-report | api | up`.
