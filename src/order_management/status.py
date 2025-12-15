STATUTS_VALIDES = {
    "CREATED": ["PAID", "CANCELLED"],
    "PAID": ["SHIPPED", "CANCELLED"],
    "SHIPPED": ["DELIVERED"],
    "DELIVERED": [],
    "CANCELLED": [],
}

def transition_statut_valide(statut_actuel: str, nouveau_statut: str) -> bool:
    if statut_actuel not in STATUTS_VALIDES:
        raise ValueError("statut actuel inconnu")
    return nouveau_statut in STATUTS_VALIDES[statut_actuel]
