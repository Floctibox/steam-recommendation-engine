# Steam Recommendation System

Projet pédagogique Python. Objectif : apprendre à concevoir, programmer et évaluer
un système de recommandation de jeux Steam. Les essais existants ne prouvent pas
la maîtrise de leurs concepts. Le développement métier attend la validation des prérequis.

## Organisation

```text
steam-recommendation-engine/
├── AGENTS.md
├── LEARNING_PROGRESS.md
├── README.md
├── pyproject.toml
├── requirements.txt
├── requirements-dev.txt
├── .gitignore
├── data/
│   ├── README.md
│   ├── raw/steam-200k.csv
│   └── processed/game_stat.csv
├── notebooks/
│   ├── 01_explo_dataset.ipynb
│   └── 02_explo_dataset.ipynb
├── src/steam_recommendation/
│   ├── __init__.py
│   └── recommendation.py
├── tests/README.md
├── models/README.md
└── docs/RESTRUCTURING_REPORT.md
```

- `data/raw` : source conservée sans transformation.
- `data/processed` : tables calculées, séparées de leur source.
- `notebooks` : exploration et essais historiques, résultats enregistrés non revalidés.
- `src/steam_recommendation` : espace des modules Python. Le prototype actuel conserve ses limites.
- `tests` : emplacement des futurs tests écrits par l'apprenant.
- `models` : futurs artefacts d'entraînement, aucun modèle actuellement.
- `docs` : décisions et audit d'architecture.

Les exercices voisins `../Part_1` restent indépendants. Aucun dossier `api`, pipeline,
configuration d'entraînement ou infrastructure cloud n'est créé sans besoin réel.
Les futures commandes iront dans `scripts/` lorsqu'elles existeront ; les paramètres
d'expérience pourront ensuite justifier `configs/`. Les transformations, représentations
d'interactions et évaluations deviendront des modules du package à mesure de l'apprentissage.

## Environnement et chemins

Au 31 octobre 2026, `python` pointe sur l'alias WindowsApps inaccessible dans la session
et `py` ne trouve aucun Python installé. Aucun environnement local n'est présent dans
le dépôt. Le kernel nommé `steam-recommendation` dans les notebooks ne prouve pas
qu'il soit disponible. La version 3.14.7 est une métadonnée historique, non vérifiée.

`requirements.txt` déclare les bibliothèques existantes et SciPy, déjà importé dans
le notebook. `requirements-dev.txt` sépare les outils facultatifs de notebook et de test.
`pyproject.toml` décrit le package sous `src` et lit les dépendances depuis le même fichier.
Aucun paquet n'a été installé. Versions non verrouillées : environnement non reproductible
à l'identique pour le moment. Choisir et vérifier un interpréteur avec l'apprenant, puis
conserver les versions réellement testées ; ne pas inventer un verrouillage.

Après accord explicite pour installer, un environnement virtuel et une installation
éditable du package permettront les imports `steam_recommendation`. Ce n'est pas
encore vérifié. Le script peut aussi être lancé par son chemin lorsque Python et
ses dépendances sont disponibles. Il charge ses CSV relativement à son fichier.

Pour les notebooks, le répertoire courant du kernel doit être `notebooks/` : vérifier
`Path.cwd()` avant leur exécution. Les chemins `../data/raw` et `../data/processed`
sont intentionnels. Le premier bloc de `02_explo_dataset.ipynb` réécrit la table calculée ;
il n'a pas été exécuté pendant l'audit. Ne pas exécuter tous les blocs pour tester
l'architecture : le dernier contient encore une erreur métier connue.

## Reprise pédagogique

Lire `AGENTS.md`, puis `LEARNING_PROGRESS.md`. Mode mentor strict : lecture du projet
autorisée ; seul le suivi pédagogique peut être modifié automatiquement. Les erreurs
existantes sont des supports de travail futurs, pas des correctifs à appliquer par l'agent.

Voir [le rapport de restructuration](docs/RESTRUCTURING_REPORT.md) et
[le dictionnaire des données](data/README.md).
