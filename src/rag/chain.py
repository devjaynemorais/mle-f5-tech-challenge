"""Cadeia RAG: retrieval + LLM (OpenAI/Gemini) restrito ao contexto do PDF."""


def answer(question: str) -> dict:
    """Retorna {answer, sources}; se o contexto não cobre a pergunta, recusa."""
    raise NotImplementedError
