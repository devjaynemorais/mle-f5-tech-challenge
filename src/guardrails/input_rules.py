"""Guardrails de entrada: palavras proibidas e tentativas de ignorar o PDF."""


def check_input(question: str) -> tuple[bool, str | None]:
    """Retorna (permitido, motivo_do_bloqueio)."""
    raise NotImplementedError
