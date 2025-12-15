import pytest
from order_management.order import calcul_total_commande

def test_calcul_total_nominal():
    assert calcul_total_commande([10.0, 5.0], [2, 1]) == 25.0

def test_calcul_total_listes_vides():
    assert calcul_total_commande([], []) == 0.0

def test_calcul_total_longueurs_diff():
    with pytest.raises(ValueError):
        calcul_total_commande([10.0], [1, 2])

def test_calcul_total_valeurs_negatives():
    with pytest.raises(ValueError):
        calcul_total_commande([10.0], [-1])
