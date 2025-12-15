import pytest
from order_management.status import transition_statut_valide

def test_transition_valide():
    assert transition_statut_valide("CREATED", "PAID") is True

def test_transition_invalide():
    assert transition_statut_valide("CREATED", "SHIPPED") is False

def test_statut_inconnu():
    with pytest.raises(ValueError):
        transition_statut_valide("UNKNOWN", "PAID")
