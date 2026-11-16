"""Schemas Pydantic: validação de entrada (Etapa 3)."""

from pydantic import BaseModel, Field


class TicketIn(BaseModel):
    """Chamado: texto não pode ser vazio nem passar de 1000 caracteres."""

    text: str = Field(min_length=1, max_length=1000)


class TriageOut(BaseModel):
    """Resultado da triagem."""

    category: str
    confidence: float


class ChatIn(BaseModel):
    """Pergunta do usuário para o RAG."""

    question: str = Field(min_length=1, max_length=1000)


class ChatOut(BaseModel):
    """Resposta do RAG (ou recusa dos guardrails)."""

    answer: str
    sources: list[str] = []
    blocked: bool = False
