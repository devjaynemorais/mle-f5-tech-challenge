"""Privacy by Design: mascara PII (CPF, e-mail, telefone) antes do LLM."""


def redact_pii(text: str) -> str:
    """Substitui PII por placeholders antes de enviar ao provedor de LLM."""
    raise NotImplementedError
