from typing import List

def calcul_total_commande(prix: List[float], quantites: List[int]) -> float:
    if len(prix) != len(quantites):
        raise ValueError("prix et quantites doivent avoir la même longueur")

    total = 0.0
    for p, q in zip(prix, quantites):
        if p < 0 or q < 0:
            raise ValueError("prix et quantites doivent être positifs")
        total += p * q

    return total
