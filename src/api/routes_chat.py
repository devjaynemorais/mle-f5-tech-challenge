"""POST /chat: guardrails de entrada, RAG sobre o PDF, guardrails de saída."""

from fastapi import APIRouter

from src.api.schemas import ChatIn, ChatOut

router = APIRouter()


@router.post("/chat", response_model=ChatOut)
def chat(body: ChatIn) -> ChatOut:
    """Responde a dúvida do usuário baseada apenas no manual em PDF."""
    raise NotImplementedError
