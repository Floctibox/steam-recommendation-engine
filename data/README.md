# Données et traçabilité

Inventaire local du 31 octobre 2026, obtenu sans modifier les CSV.

| Fichier | Contenu observé | Provenance et limites |
| --- | --- | --- |
| `raw/steam-200k.csv` | 200 000 lignes sans en-tête ; 12 393 identifiants joueur et 5 155 titres distincts | Fichier déjà présent dans le dépôt ; origine exacte et licence non documentées |
| `processed/game_stat.csv` | 3 600 lignes et en-tête | Le premier bloc du notebook 02 contient la génération correspondante ; équivalence numérique non recalculée |

Les cinq champs du brut sont nommés dans le code `id_player`, `game` (ou `Game`),
`buy?`, `playtime`, `unused`. Le troisième décrit une action `purchase` ou `play`.
Le quatrième n'est donc pas uniformément un temps de jeu : sur les lignes d'achat,
il faut interpréter la valeur selon l'action. L'unité des temps, la date de collecte
et la signification officielle de la dernière colonne restent à confirmer à la source.
Les titres servent actuellement d'identifiants de jeu ; aucun Steam app ID ni horodatage
n'est fourni dans ce schéma. Une ligne n'est pas nécessairement un jeu possédé unique.

Colonnes calculées : `Game`, `owner`, `players`, `total_playtime`, `mean_playtime`.
Le notebook compte les lignes d'achat, les lignes de jeu de durée positive et agrège
les durées des lignes `play`. Les jointures internes excluent des titres sans jeu observé.
Les nombres de lignes ne sont pas automatiquement des nombres d'utilisateurs uniques.
Les doublons, valeurs manquantes et unités nécessiteront une exploration pédagogique.

Source candidate : [Steam Video Games, tamber, Kaggle](https://www.kaggle.com/datasets/tamber/steam-video-games).
URL consultée le 31 octobre 2026, mais contenu descriptif non accessible par l'outil.
L'identité de la copie locale et les droits de redistribution ne sont pas vérifiés.
Ne pas attribuer une licence supposée ni télécharger un remplacement automatiquement.

Empreintes SHA-256, identiques avant et après déplacement :

```text
steam-200k.csv 2464A568E9B6B007D13D34E2E3A6C8DE00E5E7443F4913155F365AAA328C2874
game_stat.csv  82C949BE189D8DEB7D1D106743D0C3C3A03623CFB3B9181ACCA3132E422655A4
```

Ces deux CSV étaient déjà suivis par Git ; ce choix est préservé. Aucun nettoyage,
recalcul ou téléchargement n'a été effectué. Toute future table dérivée devra documenter
sa source, ses transformations et son protocole d'évaluation.
