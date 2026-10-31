# Audit et restructuration du 31 octobre 2026

## Périmètre et état initial

Le dossier courant `Project_Data` n'est pas un dépôt Git. Le projet est son sous-dossier
`steam-recommendation-engine`. Aucun AGENTS.md ni LEARNING_PROGRESS.md trouvé sur disque
dans cet espace malgré les onglets mentionnés. Les éventuels buffers IDE non sauvegardés
ne sont pas accessibles par cet audit ; ne pas les remplacer sans comparaison.
Git : branche `main`, suivi `origin/main`, aucun changement indexé, non indexé ou non suivi.
HEAD : `f3e2f6e`. Remote HTTPS GitHub Floctibox/steam-recommendation-engine.
Configuration locale consultée, non modifiée. Pas de commit, push, reset ou nettoyage Git.

```text
Project_Data/
├── Part_1/
│   ├── learning_panda.py
│   └── Memo Panda.docx
└── steam-recommendation-engine/
    ├── .git/
    ├── .gitignore
    ├── README.md                 (vide)
    ├── requirements.txt
    ├── data/
    │   ├── steam-200k.csv
    │   └── game_stat.csv
    ├── notebooks/
    │   ├── 01_explo_dataset.ipynb
    │   └── 02_explo_dataset.ipynb
    └── src/recommendation.py
```

Le script voisin `learning_panda.py` contient un petit DataFrame fictif, des essais
de filtres et d'agrégations commentés et un appel `isna`. Il est conservé. Le mémo
Word voisin est inventorié et préservé par empreinte ; son contenu n'a pas été audité.

## Constats

Les cinq cellules de code des deux notebooks ont été lues ainsi que leurs sorties
et métadonnées. Le premier explore et agrège les interactions. Le second produit une
table, définit une baseline excluant les jeux possédés et commence une matrice
joueur-jeu avec similarité cosinus. Une erreur TypeError est enregistrée sur `argsort`.
Le script définit une autre baseline : `player_id` n'y est pas utilisé et la sortie
est une chaîne, tandis que le notebook renvoie une table. Aucune maîtrise personnelle
ne peut être déduite de ces fichiers ou des messages de commits.

Problèmes : données sources et dérivées mélangées ; chemins dépendants du dossier courant ;
absence de documentation ; duplication divergente ; chargements CSV à l'import ;
absence de tests et de protocole d'évaluation ; SciPy importé sans déclaration directe ;
versions non verrouillées et kernel historique non vérifié. Le pivot dense avant
conversion CSR peut être coûteux en mémoire. Le comptage initial des jeux possédés
dans le notebook 01 inclut plusieurs types d'interactions. Les jointures internes
de la table calculée réduisent le catalogue. Ces problèmes métier restent à travailler.

## Architecture finale et rôle des dossiers

L'arbre complet figure dans le README racine. `data/raw` conserve la source,
`data/processed` les résultats calculés, `notebooks` l'exploration, le package
`src/steam_recommendation` les modules, `tests` les futurs tests, `models` les futurs
artefacts et `docs` les décisions. La configuration du package reste à la racine.
Pas de pipeline, API, cloud, entraînement ou nouveaux algorithmes.

## Registre exhaustif des changements

| Opération | Fichier | Raison |
| --- | --- | --- |
| Déplacé, octets identiques | `data/steam-200k.csv` → `data/raw/steam-200k.csv` | Distinguer la source |
| Déplacé, octets identiques | `data/game_stat.csv` → `data/processed/game_stat.csv` | Distinguer le calculé |
| Déplacé puis chemins adaptés | `src/recommendation.py` → `src/steam_recommendation/recommendation.py` | Package nommé ; chemins relatifs au fichier via pathlib ; corps de fonction inchangé |
| Modifié | `notebooks/01_explo_dataset.ipynb` | Chemins du brut uniquement |
| Modifié | `notebooks/02_explo_dataset.ipynb` | Chemins du brut et de l'export uniquement |
| Modifié | `.gitignore` | Ignorer caches, fichiers de build, environnement secret et futurs modèles |
| Modifié | `requirements.txt` | Déclarer SciPy déjà utilisé |
| Modifié | `README.md` | Documenter organisation, environnement, chemins et limites |
| Créé | `src/steam_recommendation/__init__.py` | Définir le package, sans algorithme |
| Créé | `pyproject.toml` | Décrire le package et réutiliser requirements.txt |
| Créé | `requirements-dev.txt` | Séparer outils de notebook et de test, aucune installation |
| Créé | `data/README.md` | Schéma, provenance incertaine et empreintes |
| Créé | `tests/README.md` | Réserver les tests et expliquer leur objectif |
| Créé | `models/README.md` | Réserver les artefacts et leur traçabilité |
| Créé | `docs/RESTRUCTURING_REPORT.md` | Conserver cet audit |
| Créé en phase 2 | `AGENTS.md` | Mentor strict permanent |
| Créé en phase 2 | `LEARNING_PROGRESS.md` | Suivi pédagogique et feuille de route |

Aucun travail supprimé. Les anciens chemins disparaissent du fait des déplacements.
Les deux CSV et tous les contenus métier sont conservés. Aucun fichier du dossier
voisin Part_1, aucune configuration Git et aucun historique n'ont été modifiés.

## Avantages et évolution

La distinction source/résultat évite de confondre observations et transformations.
Le package nommé offre une destination claire aux futurs modules sans fabriquer des
interfaces prématurées. Les dépendances ont une source unique, les outils de travail
sont séparés, les artefacts ne pollueront pas Git. La documentation expose les limites.
L'apprenant séparera progressivement chargement, préparation, représentation, classement
et évaluation lorsqu'il saura expliquer et tester chaque responsabilité.

## Vérifications et limites

Empreintes SHA-256 des CSV identiques avant/après. JSON des notebooks analysable ;
le contrôle compare les fichiers à HEAD en neutralisant uniquement les substitutions
de chemins, ce qui vérifie aussi la préservation des cellules, sorties et métadonnées.
Le corps de la fonction Python est comparé à l'original. Les chemins des notebooks
sont vérifiés depuis notebooks/ ; les deux cibles du script sont vérifiées depuis
la racine déduite de son emplacement. Git diff --check et état final sont contrôlés.

Python : alias WindowsApps inaccessible ; `py` répond « No installed Python found! ».
Aucun test Python, import réel, installation du package, entraînement ni exécution
de notebook n'a donc été réalisé. Aucune garantie de compatibilité des versions.
Les erreurs métier citées, la provenance/licence du brut, la reproductibilité exacte
et l'absence d'évaluation restent ouvertes. Aucune compétence n'est validée par cet audit.
