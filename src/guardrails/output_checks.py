"""Guardrails de saída: resposta ancorada no contexto recuperado."""


def check_output(answer: str, sources: list[str]) -> bool:
    """Retorna True se a resposta é aceitável."""
    raise NotImplementedError
