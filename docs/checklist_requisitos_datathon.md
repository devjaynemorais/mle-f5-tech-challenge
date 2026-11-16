# Checklist de requisitos: Datathon Fase 5

| Critério (peso) | Requisito | Onde | Status |
|---|---|---|---|
| Modelagem e Tracking (20%) | Escolher dataset público | `config/config.yaml` | pendente |
| | Treinar classificador (sklearn/XGBoost) | `src/classifier/train.py` | pendente |
| | Métricas (acurácia, F1) no MLflow local | `src/classifier/train.py` | pendente |
| | Endpoint de inferência FastAPI | `src/api/routes_triage.py` | pendente |
| RAG e Guardrails (30%) | `/chat` com LangChain/LlamaIndex | `src/api/routes_chat.py`, `src/rag/` | pendente |
| | PDF, chunking, vector store local (FAISS/Chroma) | `src/rag/` | pendente |
| | LLM (OpenAI/Gemini) respondendo só com base no PDF | `src/rag/chain.py` | pendente |
| | Guardrails: palavras proibidas e tentativa de ignorar o PDF | `src/guardrails/` | pendente |
| Observabilidade e Validação (20%) | Script de simulação de drift | `src/drift/simulate.py` | pendente |
| | Relatório HTML Evidently mostrando o drift | `reports/` | pendente |
| | Validação de entrada (texto vazio ou > 1000 chars) | `src/api/schemas.py` | feito (schema) |
| Nuvem e Governança (15%) | Arquitetura de nuvem no README | `README.md` | pendente |
| | Privacy by Design (LGPD) no README | `README.md`, `src/guardrails/pii.py` | pendente |
| Engenharia e Apresentação (15%) | Dockerfile + requirements.txt | raiz | esqueleto |
| | Vídeo de 5 min (STAR) | README | pendente |
