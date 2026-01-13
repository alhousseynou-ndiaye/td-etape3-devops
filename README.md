# TD – Étape 3 : DevOps & Software Engineering (Python)

## Objectif
Ce projet a pour objectif de transformer une architecture logicielle existante en un projet
Python industrialisable, intégrant :
- du packaging Python,
- des tests unitaires,
- une intégration continue (CI),
- et des règles de gouvernance Git.

---

## Structure du projet
.
├── README.md
├── pyproject.toml
├── src/
│ └── order_management/
│ ├── init.py
│ ├── order.py
│ └── status.py
├── tests/
│ ├── test_order.py
│ └── test_status.py
└── .github/
└── workflows/
└── ci.yml


---

## Fonctions métier implémentées
- **calcul_total_commande** : calcule le total d’une commande à partir des prix et quantités.
- **transition_statut_valide** : valide les transitions possibles entre statuts de commande.

---

## Installation
Créer un environnement virtuel puis installer le projet en mode développement :

```bash
pip install -e ".[dev]"


Exécution des tests

Les tests unitaires sont écrits avec pytest.
pytest

Intégration Continue (CI)

Une pipeline GitHub Actions est configurée pour :

s’exécuter automatiquement sur chaque push et pull_request,

installer le package Python,

exécuter les tests unitaires.

Le merge sur la branche main est bloqué si la CI n’est pas verte.

Gouvernance Git

La branche main est protégée :

aucun push direct n’est autorisé,

les contributions passent obligatoirement par Pull Request,

la CI GitHub Actions doit être au vert avant merge.


Conclusion

Ce projet respecte les bonnes pratiques DevOps :

packaging Python,

tests automatisés,

CI,

gouvernance Git.