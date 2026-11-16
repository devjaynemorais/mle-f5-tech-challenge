import pytest
from pydantic import ValidationError

from src.api.schemas import TicketIn


def test_ticket_vazio_e_rejeitado():
    with pytest.raises(ValidationError):
        TicketIn(text="")


def test_ticket_acima_de_1000_e_rejeitado():
    with pytest.raises(ValidationError):
        TicketIn(text="a" * 1001)


def test_ticket_valido():
    assert TicketIn(text="Meu roteador nao conecta").text
