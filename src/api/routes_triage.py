"""POST /triage: classifica o chamado com o modelo clássico."""

from fastapi import APIRouter

from src.api.schemas import TicketIn, TriageOut

router = APIRouter()


@router.post("/triage", response_model=TriageOut)
def triage(ticket: TicketIn) -> TriageOut:
    """Classifica a categoria do chamado."""
    raise NotImplementedError
