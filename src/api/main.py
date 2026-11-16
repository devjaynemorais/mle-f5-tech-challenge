"""Aplicação FastAPI: /health, /triage (Etapa 1) e /chat (Etapa 2)."""

from fastapi import FastAPI

from src.api.routes_chat import router as chat_router
from src.api.routes_triage import router as triage_router

app = FastAPI(title="Copilot de Suporte")
app.include_router(triage_router)
app.include_router(chat_router)


@app.get("/health")
def health() -> dict:
    """Liveness da API."""
    return {"status": "ok"}
