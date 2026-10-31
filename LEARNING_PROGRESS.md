# Progression en AI Engineering

## A. État général

- Dernière session : 31 octobre 2026 (Europe/Paris).
- Phase : phases 1 et 2 terminées ; phase 3, reprise pédagogique au début de la similarité utilisateur du notebook 02.
- Mode : MENTOR STRICT. Seul ce fichier peut être modifié automatiquement.
- Niveau observé : bases Python visibles (accès clé/index, boucle et compteur, résultat d'une somme filtrée correct). Précision des conditions et fonctions/retour à confirmer. L'apprenant déclare connaître les bases Python et souhaite cibler Pandas.
- Objectif actuel : concevoir les jeux candidats à partir des cinq voisins désormais associés à leurs scores.
- Prochaine étape : l'apprenant définit les ensembles de jeux observés chez les voisins et de jeux déjà possédés par le joueur cible, puis détermine les candidats par différence avant de choisir une règle de score.
- Avant toute nouvelle exploration du projet : Python de base, lecture d'erreurs, chemins, CSV et opérations Pandas à valider.
- Avant les similarités : tableaux NumPy, dimensions, vecteurs, produits scalaires, normes, cas du vecteur nul et complexité à valider.
- Avant une évaluation réelle : statistiques descriptives, séparation apprentissage/test, fuite de données et métriques de classement à valider.
- Environnement : solution trouvée le 31 octobre 2026 par appel direct à `C:/Users/Fantasy-Mine/anaconda3/python.exe` (Python 3.13.9). Pandas 2.3.3, NumPy 2.3.5, SciPy 1.16.3, scikit-learn 1.7.2 importés avec succès. Aucun paquet installé ni configuration modifiée. Les commandes python/py ne reflétaient pas les installations existantes.

## B. Compétences

Statuts de progression : **Non étudié**, **En apprentissage**, **Validé**.
Si l'historique manque, utiliser **À évaluer** comme état provisoire de connaissance,
sans inventer que le sujet est nouveau ou acquis. Une validation exige une réalisation
autonome, une explication et un cas nouveau ou limite. « J'ai compris » ne suffit pas.

| Domaine | Compétences à vérifier | Statut | Exercices/preuves disponibles | Difficultés et validation |
| --- | --- | --- | --- | --- |
| Programmation Python | Types, listes, dictionnaires, ensembles, boucles, conditions, fonctions, exceptions, complexité | En apprentissage | D1 : distinction clé/index correcte ; total 9 correct ; boucle/compteur proposés | Confusion dans l'explication du seuil ; >= 0 inclut zéro ; fonction/return et cas vide non fournis. Validation autonome sur cas nouveau encore attendue |
| NumPy et Pandas | shape, indexation, masques, agrégation, jointure, pivot, axes | En apprentissage | Notebooks relus et exécutés en copie temporaire ; P1 : groupby/count interprété, filtre purchase/groupby proposés, `.nunique()` identifié après indice ; P2 : jointures interne/gauche, expansion 2 × 2 et unicité après groupby correctement expliquées | Pivot, axes, syntaxe `how`/`on` et interprétation des zéros à confirmer |
| Mathématiques et algèbre linéaire | Vecteurs, matrices, produit scalaire, norme, cosinus, matrices creuses | À évaluer | Aucun exercice évalué | À déterminer |
| Probabilités et statistiques | Moyenne, médiane, dispersion, échantillonnage, probabilités conditionnelles | À évaluer | Moyennes/médiane présentes dans un notebook, sans preuve d'explication | À déterminer |
| Manipulation et préparation des données | Schéma CSV, types, doublons, valeurs manquantes, unités, comptages, séparation des données | En apprentissage | P1 : distingue lignes d'achat et lignes de jeu ; résultats bruts corrects ; reconnaît qu'un doublon ne crée pas de nouveau titre ; `.nunique()` trouvé après indice ; P2 : pertes/valeurs manquantes, quatre paires sur clé dupliquée et rôle du groupby dans le notebook expliqués | Confirmer le grain et le sens des absences dans la matrice joueur-jeu |
| Machine Learning | Baseline, apprentissage/test, généralisation, surapprentissage, fuite | À évaluer | Aucun exercice évalué | À déterminer |
| Systèmes de recommandation | Popularité, feedback implicite, filtrage collaboratif, user-user/item-item, cold start, métriques | En apprentissage | Baselines et essai cosinus présents ; l'apprenant demande explicitement de reprendre la similarité du notebook 02, sans preuve de maîtrise du calcul | Vérifier score cosinus, tri, indices, auto-similarité et traduction en recommandations |
| AI Engineering et MLOps | Séparation des responsabilités, pipelines, reproductibilité, artefacts, suivi d'expériences | À évaluer | Restructuration effectuée par le mentor, pas par l'apprenant | Ne constitue pas une preuve de maîtrise |
| Outils professionnels | Terminal, Git, environnement virtuel, dépendances, kernel, tests, lecture de documentation | À évaluer | Dépôt Git présent, aucun exercice évalué | Python non disponible dans la session |

## C. Historique des sessions

### 2026-10-31 — Audit, organisation et diagnostic proposé

- Concepts présentés : séparation brut/calculé, package Python, dépendances de développement, rôle des tests et des artefacts.
- Travail de l'agent : audit, déplacements conservateurs, chemins, documentation, configuration du mentor ; voir docs/RESTRUCTURING_REPORT.md.
- Travail de l'apprenant pendant cette session : aucun exercice reçu à ce stade.
- Diagnostic D1 : expliquer liste/dictionnaire, prévoir l'accumulation filtrée sur `[0, 2, 5, 2]`, puis écrire une fonction qui compte les valeurs strictement positives et expliquer le cas vide.
- Erreurs observées dans l'existant : TypeError enregistré sur argsort, baseline du script ignorant player_id, confusion possible entre lignes et jeux possédés. Ce ne sont pas des erreurs diagnostiquées chez l'apprenant pendant cette session.
- Compétences validées : aucune.
- Difficultés personnelles : À évaluer ; environnement indisponible comme limitation technique.
- Décision : suspendre tout nouveau développement métier jusqu'à validation des bases nécessaires. Activation permanente du mode mentor strict après création des règles.

### 2026-10-31 — Réponses D1, orientation Pandas et exécution débloquée

- D1.1 : distinction clé/index correcte, sans validation globale des structures.
- D1.2 : résultat 9 correct ; explication « dès que heures > 0 » imprécise : condition réelle `valeur > 1`. Le seul résultat sur cette liste ne distingue pas ces seuils.
- D1.3 : boucle et compteur proposés ; `>= 0` inclut zéro. Script avec print, sans fonction ni return ; cas vide non expliqué. Ne pas en déduire une incapacité générale à écrire des fonctions.
- Retour : préciser seuil et différence affichage/retour, sans fournir la solution complète.
- Préférence : l'apprenant déclare connaître les bases Python et souhaite travailler Pandas à partir de ses notebooks.
- Parcours ajusté : comptages, grain des données, filtres, puis jointures ; NumPy/axes/tri et mathématiques avant reprise du cosinus. M1 devient un ensemble de vérifications ponctuelles.
- Diagnostic P1 proposé : table fictive contenant achat et jeu pour un même titre ; expliquer groupby/count puis proposer un comptage Pandas des titres possédés uniques après filtre purchase.
- Autorisation ponctuelle : modifications de fichiers nécessaires à l'exécution côté agent permises par l'utilisateur. Aucune modification technique nécessaire ; mode mentor strict maintenu.
- Solution : Anaconda Python 3.13.9 hors PATH, appelé par chemin complet avec `-B`. Python 3.14.6 également trouvé sous AppData/Local/Python/pythoncore-3.14-64 mais sans SciPy/sklearn, non retenu.
- Exécution : les trois cellules du notebook 01 et la première du notebook 02 réussissent. La dernière cellule reproduit TypeError sur argsort. Matrice : 11 350 × 3 600.
- Sources exécutées dans un dossier temporaire avec copies des CSV. Export seulement dans cette copie ; table recalculée égale à l'existante selon DataFrame.equals. Script chargé avec succès depuis un dossier courant indépendant. Empreintes des notebooks, CSV et sources inchangées.
- Limite : exécution par Python, pas validation d'un kernel Jupyter dans l'IDE. Aucun correctif métier, installation ou changement du PATH.
- Compétences globalement validées : aucune ; preuves partielles de bases Python consignées.

### 2026-10-31 — Diagnostic Pandas P1 : comptage des achats

- Réponse 1 : `groupby("id_player")["game"].count()` donne 3 pour le joueur 10 et 1 pour le joueur 20 ; correct, sous réserve de valeurs non manquantes dans la colonne game.
- Réponse 2 : l'apprenant explique qu'un jeu possédé correspond à une action purchase ; il ne chiffre pas explicitement 2 titres pour le joueur 10 et 1 pour le joueur 20.
- Réponse 3 : filtre purchase puis groupby et count proposés correctement pour compter les lignes d'achat. Cette expression ne protège pas contre un achat dupliqué d'un même titre, exigence de l'exercice.
- Acquis partiels : lecture d'un comptage groupé et filtre conditionnel. À travailler : grain de l'observation, déduplication, différence entre `count()` et nombre de valeurs uniques.
- Prochain mini-exercice : ajouter une deuxième ligne `purchase` pour Portal/joueur 10 ; prédire le résultat du code proposé, le nombre de titres réellement distincts, puis nommer et employer l'agrégation adaptée. Ne pas fournir de solution complète avant la tentative.
- Compétences validées : aucune nouvelle validation globale.

### 2026-10-31 — Diagnostic Pandas P1 : tentative sur le doublon

- L'apprenant répond que le résultat de son expression resterait identique pour le joueur 10 et que le nombre de jeux possédés resterait identique. La seconde intuition est correcte (Portal et Terraria demeurent deux titres) ; la première confond lignes d'achat et titres distincts.
- Proposition de méthode : « value.count » (hypothèse). Vérifier la distinction entre comptage de toutes les lignes, fréquence de chaque titre et nombre de titres uniques. Ne pas attribuer une maîtrise de la méthode.
- Retour prévu : avec deux lignes purchase pour Portal et une pour Terraria, son `count()` renvoie 3 ; le nombre de titres distincts reste 2. `value_counts()` donnerait une fréquence par titre. Indice : chercher une méthode Pandas dont le nom combine « number » et « unique ».
- Compétences validées : aucune nouvelle validation globale. Prochaine réponse : demander à l'apprenant de modifier seulement l'agrégation finale et d'expliquer le résultat.

### 2026-10-31 — Diagnostic Pandas P1 : méthode des valeurs distinctes

- Réponse : `.nunique()` identifiée correctement après indice pour compter les titres distincts au sein de chaque groupe.
- Preuve : choix de la méthode adaptée ; l'expression complète et un cas nouveau ne sont pas encore produits. Ne pas valider tout le domaine Pandas sur ce seul exercice.
- Prochaine étape : jointure interne de deux petites tables de jeux, compter les lignes résultantes et expliquer le sort d'un jeu présent uniquement à gauche. Relier ensuite au `merge` du notebook 02.
- Compétences validées : aucune nouvelle validation globale ; sous-concept « choisir nunique pour les valeurs distinctes » observé avec aide.

### 2026-10-31 — Diagnostic Pandas P2 : jointure interne

- Réponse : sur les tables achats (Portal, Terraria, Celeste) et temps de jeu (Portal, Terraria), l'apprenant prédit deux lignes et la disparition de Celeste, car absent de la seconde table. Correct et expliqué sans indice.
- Preuve : compréhension du comportement par défaut de `merge` sur clés uniques de cet exemple. Cardinalités avec doublons et jointure gauche non encore évaluées.
- Suite proposée : prévoir le résultat d'une jointure gauche, notamment le sort de Celeste et la valeur de `total_playtime`, puis identifier le paramètre `how`.
- Compétences validées : sous-concept jointure interne sur clés uniques observé ; pas de validation globale de Pandas.

### 2026-10-31 — Diagnostic Pandas P2 : jointure gauche

- L'apprenant propose toujours `merge` avec une jointure left et indique que Celeste serait conservé ; il prévoit `NaN` pour `total_playtime` sauf remplacement explicite par une valeur choisie. Compréhension conceptuelle correcte.
- Précision nécessaire : `how="left"` sélectionne le type de jointure ; `on="game"` désigne la clé commune lorsque les deux colonnes portent le même nom ; `left_on` seul ne sélectionne pas le type de jointure et s'utilise avec `right_on` si les noms diffèrent. L'exemple fictif comporte trois lignes en sortie avant éventuels doublons.
- Preuve partielle : comportement de la jointure gauche et des valeurs manquantes expliqué ; syntaxe exacte et cardinalité avec doublons encore à confirmer. Ne pas valider tout Pandas.
- Suite : court exercice de cardinalité avec une clé présente deux fois à gauche et deux fois à droite, puis relier ce risque aux `merge` du notebook 02.

### 2026-10-31 — Diagnostic Pandas P2 : doublons des deux côtés

- Réponse : l'apprenant suppose que la première occurrence de Portal à gauche se combine seulement à la première à droite, puis les autres par rang. Cette hypothèse ne correspond pas à `merge` sur une clé dupliquée.
- Indice suivant : nommer les deux lignes Portal gauches G1/G2 et les deux droites D1/D2 ; pour G1, identifier toutes les lignes droites ayant la clé Portal, puis refaire pour G2 et compter les paires.
- Point pédagogique : la jointure utilise l'égalité des clés, pas la position des lignes. La cardinalité peut dépasser celle de chaque entrée. Ne pas valider le concept avant une prédiction correcte sur les paires.
- Compétences validées : aucune nouvelle validation.

### 2026-10-31 — Diagnostic Pandas P2 : correction de la cardinalité

- Après indice G1/G2 et D1/D2, l'apprenant énumère correctement G1–D1, G1–D2, G2–D1, G2–D2 et conclut à quatre lignes. Il explique le principe de toutes les correspondances possibles sur la clé.
- Preuve : cardinalité 2 × 2 maîtrisée sur l'exemple avec aide ; application à une nouvelle table encore à observer. Pas de validation globale du domaine Pandas.
- Prochaine question : dans le notebook 02, les trois tables sont regroupées par `game` avant `merge`. Demander pourquoi ce `groupby` empêche en principe les quatre combinaisons pour un même jeu, tout en laissant possible l'exclusion d'un jeu sans correspondance en jointure interne.

### 2026-10-31 — Diagnostic Pandas P2 : tables agrégées du notebook

- Réponse : l'apprenant explique que chaque table issue de `groupby("game")` contient une seule occurrence par jeu ; la jointure des trois agrégats ne produit donc qu'une ligne pour chaque jeu présent dans les trois tables. Correct sur la cardinalité et relié au code réel.
- Nuance gardée : la jointure interne peut malgré tout exclure un jeu absent d'un des agrégats ; ceci a été compris dans l'exercice précédent. Aucun code métier modifié.
- Preuve : explication autonome sur le notebook après un exercice guidé ; sous-concepts `groupby` et cardinalité des jointures observés. La compétence Pandas globale reste En apprentissage.
- Suite : `pivot_table` du notebook 02, dimensions et sens de `fill_value=0` dans les interactions implicites.

### 2026-10-31 — Changement de rythme demandé par l'apprenant

- L'apprenant indique que les exercices Pandas deviennent redondants pour lui et souhaite reprendre le début du moteur de recommandation au point d'arrêt du notebook 02. La question sur `pivot_table` est écartée comme exercice séparé ; ses implications seront traitées seulement si elles bloquent la similarité.
- Le dernier bloc du notebook 02 est relu en lecture seule. `cosine_similarity(user_vector, user_game_sparse)` produit un score par joueur ; la sortie enregistrée est de forme `(11350,)` après `flatten`. Le `TypeError` se produit sur `similarities.argsort(similarities, False)`.
- Documentation officielle vérifiée pour les versions en usage : `ndarray.argsort(axis=-1, kind=None, order=None)` dans NumPy 2.3 ; `cosine_similarity(X, Y)` retourne une matrice `(n_samples_X, n_samples_Y)` dans scikit-learn 1.7.
- Décision pédagogique : expliquer les formes et la cause de l'erreur, puis demander à l'apprenant de proposer lui-même l'étape de tri et l'interprétation des indices. Pas de correction automatique du notebook ni de code métier fourni prêt à copier.
- Compétences validées : aucune nouvelle validation globale.

### 2026-10-31 — Nouveau blocage dans le notebook 02

- Modification de l'apprenant observée sur disque en lecture seule : `similarities.argsort(0,False)` remplace l'appel précédent. Le notebook porte désormais le kernelspec `python3`, métadonnée Python 3.14.6.
- Sortie enregistrée : `ModuleNotFoundError: No module named 'scipy'` sur `from scipy.sparse import csr_matrix`, avant toute exécution de la fonction de similarité. Le problème immédiat est le kernel/environnement.
- Interpréteurs vérifiés sans installation : `C:/Users/Fantasy-Mine/AppData/Local/Python/pythoncore-3.14-64/python.exe` n'a ni ipykernel, ni SciPy, ni scikit-learn ; `C:/Users/Fantasy-Mine/anaconda3/python.exe` (3.13.9) dispose d'ipykernel, SciPy et scikit-learn.
- Conseil pédagogique : sélectionner Anaconda Python 3.13.9 comme kernel du notebook dans l'IDE, puis contrôler `sys.executable`. Ne pas installer SciPy dans un autre interpréteur sans besoin.
- Deuxième problème déjà établi par essai local isolé : sur NumPy 2.3.5, `similarities.argsort(0, False)` produit `TypeError: sort kind must be str, not bool`. Le deuxième argument positionnel est `kind`, pas un drapeau de tri décroissant. Guider l'apprenant pour la correction, sans réécrire son code.
- La commande de découverte Jupyter `python -m jupyter kernelspec list` n'a pas abouti dans le sandbox car elle voulait créer `C:\Users\Fantasy-Mine\.jupyter` hors de l'espace autorisé ; aucune modification du projet effectuée par cette commande. La présence d'ipykernel Anaconda a été vérifiée séparément.
- Compétences validées : aucune nouvelle validation.

### 2026-10-31 — Vérification du kernel actif dans l'IDE

- L'apprenant confirme que `sys.executable` affiche `C:\Users\Fantasy-Mine\AppData\Local\Python\pythoncore-3.14-64\python.exe` ; il s'agit toujours de l'interpréteur sans SciPy, ce qui explique la persistance du `ModuleNotFoundError`.
- Vérification répétée en lecture seule : `C:\Users\Fantasy-Mine\anaconda3\python.exe` importe SciPy 1.16.3, scikit-learn et ipykernel ; Python 3.14.6 sous AppData ne trouve pas SciPy.
- Étape suivante : sélectionner explicitement Anaconda comme kernel du notebook dans l'IDE, redémarrer/relancer la cellule, puis confirmer le nouveau `sys.executable`. Aucun paquet installé, aucun réglage de projet modifié.

### 2026-10-31 — Kernel corrigé, nouvelle erreur sur argsort

- L'apprenant confirme avoir réglé son kernel Python. Le notebook enregistré porte désormais `base` / Python 3.13.9 ; l'import SciPy passe et la cellule imprime `(11350,)` avant l'erreur.
- Tentative observée : `similarities.argsort(0, order=False)`. Erreur enregistrée : `ValueError: Cannot specify order when the array has no fields.`
- Cause : le paramètre `order` de `ndarray.argsort` sert au tri des champs d'un tableau structuré, pas au choix croissant/décroissant ; le tableau de similarités contient des nombres simples. L'axe `0` est valable pour ce vecteur 1D mais inutile à préciser.
- Explication pédagogique donnée avec un petit vecteur numérique indépendant : `argsort` fournit les positions en ordre croissant ; inverser ces positions fournit l'ordre décroissant, sans altérer l'alignement avec les identifiants des joueurs.
- Prochaine preuve attendue : l'apprenant adapte lui-même la ligne de son notebook, vérifie les premières positions/scores puis explique comment récupérer les vrais identifiants et exclure l'auto-similarité.
- Compétences validées : aucune nouvelle validation globale.

### 2026-10-31 — Tri des similarités en cours

- L'apprenant reformule correctement l'objectif : classer les scores de similarité par ordre décroissant pour trouver les profils les plus proches.
- Notebook observé en lecture seule : `similarities.argsort(0)` s'exécute maintenant sans erreur et renvoie 11 350 positions. La sortie enregistrée commence par `[5674 7348 7349 ...]` et finit par `[..., 1315 1974 1]` ; elle est encore en ordre croissant des scores.
- Distinction à conserver : les valeurs renvoyées sont des positions dans `game_played`, pas les identifiants Steam ; le joueur requête figure parmi les candidats et doit être exclu explicitement avant de choisir ses voisins.
- Aide suivante : demander à l'apprenant d'inverser le tableau de positions, puis d'inspecter les scores correspondants et l'identifiant de la première position. Ne pas remplacer son code.
- Compétences validées : compréhension du sens souhaité du tri observée ; tri et interprétation des résultats pas encore validés.

### 2026-10-31 — Association des scores aux identifiants joueurs

- L'apprenant propose un `merge` entre le résultat de `similarities` et l'index des joueurs pour retrouver le taux et le joueur le plus similaire.
- Diagnostic sur la cellule enregistrée : `similarities` contient d'abord les scores, puis est écrasé par `similarities.argsort(0)` ; après cette affectation, ce sont des positions triées, les scores ont été perdus dans cette variable. `game_played.index`, les lignes de `user_game_sparse` et les scores sont déjà alignés par position ; une jointure n'est pas nécessaire.
- Explication à donner : pour une position `i`, le score est la valeur de la liste de scores à `i` et l'identifiant du joueur est `game_played.index[i]`. Garder des variables distinctes pour scores et ordre de tri ; éviter de fournir la solution complète de la fonction.
- Compréhension à confirmer : ordre décroissant, correspondance position/score/id, exclusion de l'utilisateur lui-même avant sélection des voisins.
- Compétences validées : aucune nouvelle validation globale.

### 2026-10-31 — Tentative de sélection d'un voisin

- Code lu sans modification : `pos_player_simil = similarities.argsort(0)` puis `return similarities[pos_player_simil[1]]`. La cellule affiche `(11350,)` puis `0.0`.
- L'apprenant décrit l'intention de prendre « l'avant-dernier » afin d'éviter le joueur lui-même. Le code utilise l'indice `[1]` du classement croissant : deuxième score le plus faible, d'où 0.0. Cette sortie est un score seul, pas un identifiant joueur.
- Nuance : l'auto-similarité d'un vecteur non nul vaut en principe 1, mais un autre profil peut être identique ou presque identique ; un tri ne garantit pas que le joueur requête soit exactement le dernier en cas d'égalité. L'exclusion doit comparer les positions à `player_index`.
- Explication à donner : les indices négatifs accèdent à la fin d'un tableau ; pour toute position `p` retenue, `similarities[p]` donne le score et `game_played.index[p]` donne l'identifiant. Ne pas fournir la fonction complète.
- Compétences validées : aucune nouvelle validation globale ; l'apprenant a séparé scores et positions, point de progrès concret.

### 2026-10-31 — Sélection du premier voisin, cas du joueur 76767

- Code de l'apprenant observé : `pos_player_simil = similarities.argsort(0)` puis `return game_played.index[pos_player_simil[-2]]`. La sortie enregistrée est `77542968` pour `player_id=76767` ; l'apprenant demande si cela fonctionne.
- Vérification indépendante en lecture seule avec les CSV locaux et l'interpréteur Anaconda : le dernier classement est la position 1, id 76767, score 1.0000000000000002 ; l'avant-dernier est la position 1974, id 77542968, score 0.7423939829402133. Le résultat est correct pour ce joueur précis.
- Limite de généralisation : utiliser systématiquement `[-2]` suppose que le joueur requête est dernier. D'autres profils peuvent avoir un score identique ou presque égal, et l'ordre des égalités n'assure pas cette position. Exclure explicitement la position `player_index` avant de prendre le meilleur voisin.
- Le code retourne seulement un `id_player`, sans score ; acceptable pour l'objectif immédiat de retrouver un premier voisin, mais les scores devront être accessibles pour comprendre et comparer les recommandations.
- Preuve : compréhension et application autonome de `argsort`, index négatif et conversion position → identifiant sur un cas réel ; robustesse multi-utilisateur encore à construire. Aucune compétence globale de recommandation validée.

### 2026-10-31 — Question sur l'exclusion du joueur et les cinq voisins

- L'apprenant demande comment exclure explicitement `player_index` et obtenir les cinq joueurs de similarité maximale ; il propose `.head()` à partir d'une position.
- Guidance : `pos_player_simil` est un ndarray NumPy, donc pas de `.head()` ; utiliser le découpage `[:5]` sur une séquence déjà classée du meilleur au moins bon. Exclure `player_index` par un masque de comparaison appliqué au tableau de positions. Conserver `similarities` pour obtenir les scores et `game_played.index` pour obtenir les identifiants.
- Clarification : le cosinus donne une similarité, pas une probabilité. Ne pas retirer automatiquement la dernière position, car l'auto-similarité peut être à égalité avec un autre profil.
- Étape attendue : l'apprenant modifie sa cellule et explique les cinq premiers couples (identifiant, score) avant d'aller vers les jeux candidats. Pas de code métier écrit par le mentor.

### 2026-10-31 — Tentative de classement des voisins

- Cellule de l'apprenant lue sans modification : `pos_player_simil = np.sort(similarities.argsort(0))[::-1]`, puis `return game_played.index[pos_player_simil[1]]`. Sortie enregistrée : `309824202`; tous les scores sont imprimés.
- Diagnostic : `similarities.argsort(0)` ordonne correctement les positions selon les scores croissants, mais `np.sort(...)` retrie ces positions selon leurs numéros et détruit ce classement. `[::-1]` inverse ensuite les numéros de position, pas l'ordre des similarités. La sortie n'établit donc pas le voisin le plus proche.
- Étapes encore manquantes : enlever ce second tri, exclure explicitement `player_index`, prélever cinq positions et associer chacune à son score et à `game_played.index`. Éviter d'imprimer les 11 350 scores pendant le diagnostic.
- Aide prévue : expliquer pourquoi `np.sort` est de trop et inviter l'apprenant à comparer les scores des premières positions après sa correction ; ne pas modifier le notebook à sa place.
- Compétences validées : aucune nouvelle validation globale.

### 2026-10-31 — Cinq voisins obtenus sur un joueur

- Cellule de l'apprenant lue en lecture seule : `pos_player_simil = similarities.argsort(0)[::-1]` puis `return game_played.index[pos_player_simil[1:6]]`. Le second `np.sort` a été supprimé : l'ordre par score est préservé et inversé.
- Sortie enregistrée pour `player_id=76767` : cinq identifiants `[77542968, 58297398, 45459546, 53784377, 9209946]`. Les deux premiers concordent avec la vérification indépendante précédente ; le premier joueur requête occupait la première position sur cet exemple.
- Limite : `[1:6]` élimine toujours le premier rang, sans tester son identifiant. En cas d'égalité ou d'un autre utilisateur, cela peut inclure le joueur requête et exclure un vrai voisin. La sélection générale nécessite un masque sur les positions `!= player_index`, puis `[:5]`.
- Présentation : la cellule imprime le tableau entier de 11 350 scores, peu utile pour vérifier les cinq résultats. Préférer afficher seulement les scores correspondant aux cinq positions retenues.
- Acquis démontré : inversion correcte du résultat d'argsort et découpe de cinq éléments, traduction en cinq identifiants sur un cas réel. Exclusion robuste de soi et lien score/identifiant encore à démontrer.

### 2026-10-31 — Stratégie d'exclusion du joueur requête

- L'apprenant propose de parcourir les premières positions avec une boucle pour détecter/supprimer `player_index`, puis demande une option NumPy plus simple et rapide.
- Concept introduit : comparaison élément par élément d'un ndarray de positions avec `player_index`, produisant un masque booléen ; appliquer ce masque au tableau de positions conserve tous les indices différents. Filtrer avant `[:5]`, sinon la liste peut n'avoir que quatre voisins après exclusion.
- Clarification : comparer une position de `pos_player_simil` à `player_index`, et non directement à l'identifiant Steam `player_id`. `.head()` relève de Pandas ; le découpage `[:5]` relève du tableau NumPy utilisé ici.
- Réponse pédagogique : exemple indépendant sur un petit ndarray ; l'apprenant adaptera lui-même le code du notebook. Aucune correction automatique.
- Compétences validées : aucune nouvelle validation globale.

### 2026-10-31 — Masque appliqué à la mauvaise valeur

- Code de l'apprenant : `masque = pos_player_simil != player_id`, puis `pos_player_simil = pos_player_simil[masque]` avant `[:5]`. Le filtrage est placé au bon moment, mais compare des positions à un identifiant Steam.
- Sortie enregistrée : `[76767, 77542968, 58297398, 45459546, 53784377]` ; le joueur requête est encore présent.
- Cause concrète : pour `player_id=76767`, `game_played.index.get_loc(player_id)` donne la position `1` (vérification indépendante précédente). La position `1` ne vaut pas `76767`, donc le masque la conserve. Le tableau contient des positions ; comparer à `player_index`.
- Guidance : demander à l'apprenant de changer la variable de comparaison, puis de contrôler l'absence de son identifiant dans les cinq résultats. Aucune correction automatique du notebook.
- Compétences validées : masque et filtrage appliqués, mais distinction identifiant/position encore en apprentissage.

### 2026-10-31 — Exclusion robuste et passage aux candidats

- Code observé en lecture seule : `masque = pos_player_simil != player_index`, application du masque avant `[:5]`, puis conversion des cinq positions par `game_played.index[...]`.
- Sortie enregistrée pour `76767` : `[77542968, 58297398, 45459546, 53784377, 9209946]` ; l'identifiant requête n'y figure plus. La correction répond au problème précédent pour ce cas. Aucun changement apporté au notebook par le mentor.
- Acquis observés : tri décroissant des positions, masque sur position plutôt qu'identifiant, sélection de cinq autres joueurs. Vérifier encore les scores associés et tester d'autres utilisateurs avant validation globale.
- Prochaine activité pratique : garder les scores des cinq positions, puis construire conceptuellement des jeux candidats à partir des voisins, en excluant les jeux déjà possédés. Ne pas choisir une formule de classement ou écrire du code de recommandation pour l'apprenant.

### 2026-10-31 — Voisins et scores associés

- Code de l'apprenant lu en lecture seule : `list(zip(game_played.index[pos_player_simil[:5]], similarities[pos_player_simil[:5]]))`. Les mêmes positions sont utilisées pour identifiants et scores après exclusion du joueur cible.
- Sortie enregistrée pour `76767` : (77542968, 0.7423939829402133), (58297398, 0.688081445991098), (45459546, 0.6868979156240458), (53784377, 0.6868636770408264), (9209946, 0.6867058652513046). Les scores sont décroissants et l'utilisateur cible est absent.
- Sous-concept de sélection des cinq voisins avec scores validé sur ce cas réel, grâce au code écrit par l'apprenant. Pas de validation de l'ensemble des systèmes de recommandation avant tests sur d'autres joueurs et conception des candidats/évaluation.
- Correction conceptuelle à guider : le commentaire `flatten() #on arroundi` est inexact. `flatten()` convertit la forme `(1, n)` en `(n,)` ; il n'arrondit pas les valeurs. L'apprenant corrige son commentaire lui-même.
- Suite : identifier les jeux possédés ou joués par les voisins, exclure ceux déjà possédés par l'utilisateur cible, puis débattre du classement des candidats. Aucun code métier modifié par le mentor.

## D. Ressources externes et locales

Vérification au 31 octobre 2026. Ne pas confondre documentation officielle accessible,
présence locale d'un fichier et provenance de son téléchargement effectivement prouvée.

| Ressource | Utilité et moment | Provenance vérifiée / limites | Contraintes |
| --- | --- | --- | --- |
| `data/raw/steam-200k.csv` | Exploration après M1–M3 ; interactions joueur-jeu | Présence locale et SHA-256 vérifiés ; origine distante exacte inconnue | 5 champs sans en-tête ; sens des unités, collecte et licence à confirmer |
| `data/processed/game_stat.csv` | Comprendre les agrégations puis la baseline | Présence locale ; génération visible dans notebook 02, non réexécutée | Table historique de 3 600 lignes ; ne pas confondre avec la source |
| [Steam Video Games — Kaggle](https://www.kaggle.com/datasets/tamber/steam-video-games) | Candidat pour retrouver la fiche du dataset existant | URL consultée, texte non accessible ; correspondance avec la copie locale non vérifiée | Licence et attribution à vérifier, aucun téléchargement automatique |
| [Tutoriel Python officiel](https://docs.python.org/3/tutorial/) | Référence M1, extraits ciblés accompagnés | Site officiel consulté | Prévoit déjà quelques bases de programmation ; adapter les explications, ne pas demander une lecture intégrale |
| [Prise en main Pandas](https://pandas.pydata.org/docs/getting_started/index.html) | Tables, CSV, filtres et agrégations en M3 | Documentation officielle consultée ; pandas déclaré localement | Vérifier ensuite la version réellement installée ; licence du paquet à consulter avant redistribution |
| [Bases NumPy](https://numpy.org/doc/stable/user/absolute_beginners.html) | Tableaux et dimensions en M2 | Documentation officielle consultée ; numpy déclaré localement | Ne pas traiter automatiquement une liste comme un ndarray ; version locale inconnue |
| SciPy | Matrices creuses après M4 | Import csr_matrix constaté dans notebook 02 ; ajouté à requirements.txt | Aucun paquet installé ; documentation/version/licence à vérifier au module concerné |
| scikit-learn | Similarité puis métriques après fondements | Déclaré dans requirements.txt ; cosine_similarity importé dans notebook 02 | Ne pas utiliser une API sans comprendre entrées/sorties ; version locale inconnue |
| Matplotlib | Visualiser les distributions en M5 | Déclaré dans requirements.txt, aucun usage dans les cellules auditées | Facultatif avant visualisation ; documentation/version/licence à vérifier plus tard |
| Git et terminal | Historique, diffs, chemins dès M1 | Git local fonctionnel ; dépôt et configuration consultés | Éviter les opérations destructives ; pas de commit automatique pendant la session |
| Python, venv, pip | Environnement et exécution | Anaconda Python 3.13.9 trouvé puis utilisé par chemin absolu ; alias WindowsApps et launcher py insuffisants | Aucun environnement créé ; accord requis avant installation |
| JupyterLab et ipykernel | Exécution interactive après M1 | Déclarés seulement dans requirements-dev.txt ; kernel historique nommé steam-recommendation | Installation non effectuée ; vérifier le dossier courant notebooks/ |
| pytest | Tests de fonctions lors de M7 | Déclaré seulement dans requirements-dev.txt | Pas de tests métier actuels ni d'installation ; petits cas fictifs d'abord |
| Journal d'expériences simple | Données, paramètres, métriques, versions en M7 | Besoin futur documenté dans models/README.md | Un tableau suffit au départ ; aucun outil spécialisé imposé |
| Outil API / déploiement | Seulement après système évalué et besoin utilisateur explicite, M8 | Aucun outil choisi ni installé | Comparer les options à ce moment, expliquer leur utilité avant adoption |

Le dictionnaire et les empreintes des CSV sont dans `data/README.md`. Aucune méthode
d'évaluation n'est encore en place ; M6 introduira séparation des interactions,
Precision@K/Recall@K et comparaison à une baseline avec leurs limites.

## E. Feuille de route provisoire

Parcours à personnaliser après D1 puis de petits diagnostics successifs. Pas de
calendrier imposé. Chaque module suit : intuition, théorie, intérêt Steam, petit
exemple fictif, question, exercice, retour et évaluation sur un cas nouveau.

### M1 — Python et outils de base (avant développement)

- Compétences : structures, contrôle de flux, fonctions, erreurs, chemins, environnement et Git élémentaire.
- Intérêt : lire et traiter une collection d'interactions sans dépendre d'une bibliothèque.
- Prérequis : aucun acquis supposé ; commencer par D1.
- Théorie : types, mutabilité, itération, portée, paramètres/retour, coût d'une boucle.
- Exercices : D1 puis filtrer une petite liste fictive et expliquer un message d'erreur ; distinguer fichier et dossier courant.
- Erreurs courantes : indice/valeur, print/return, compteur/somme, alias de listes, cas vide oublié.
- Évaluation : fonction courte autonome, explication ligne par ligne et cas limite, lecture d'un diff.
- Passage : résultat justifié sur cas normal, vide et frontière ; corriger soi-même une erreur après indice.

### M2 — NumPy et représentation tabulaire (avant similarités)

- Compétences : ndarray, shape, axes, indexation, masques et opérations vectorisées.
- Intérêt : savoir ce que représente une ligne joueur et une colonne jeu.
- Prérequis : M1.
- Théorie : tableau homogène, dimensions, sélection et coût mémoire.
- Exercices : prédire les formes et extraire des valeurs d'une matrice fictive 2 × 3.
- Erreurs courantes : axe inversé, index confondu avec identifiant, dimensions incompatibles.
- Évaluation : prédictions sans exécution puis explication des résultats.
- Passage : expliquer chaque dimension et choisir correctement lignes/colonnes sur un exemple nouveau.

### M3 — Pandas et qualité des données (avant exploration réelle)

- Compétences : CSV, schéma, types, filtres, groupby, merge, doublons et valeurs manquantes.
- Intérêt : distinguer achat, session/observation de jeu, joueur et jeu unique.
- Prérequis : M1 ; notions de tables de M2.
- Théorie : grain d'une ligne, clé, cardinalité d'une jointure, count/size/nunique, données dérivées.
- Exercices : petite table fictive avec un doublon et une valeur absente ; calcul manuel puis Pandas.
- Erreurs courantes : additionner achats et durées, compter des lignes comme des personnes, perdre des lignes en jointure.
- Évaluation : expliquer les variations de cardinalité et les résultats agrégés.
- Passage : produire et justifier une table correcte, identifier les ambiguïtés ; ensuite seulement explorer le CSV Steam.

### M4 — Algèbre linéaire et similarité (avant filtrage collaboratif)

- Compétences : vecteurs, matrices, produit scalaire, norme, cosinus, parcimonie.
- Intérêt : comparer les profils joueur-jeu avec un sens mathématique.
- Prérequis : M2, opérations arithmétiques et racine carrée évaluées au début du module.
- Théorie : somme des produits, longueur euclidienne, normalisation, angle, vecteur nul ; dense/creux.
- Exercices : calculer à la main sur deux petits vecteurs, analyser une multiplication d'échelle.
- Erreurs courantes : cosinus confondu avec distance, division par zéro, scores confondus avec indices de tri.
- Évaluation : expliquer le calcul, ses limites et un cas nouveau ; estimer le nombre d'éléments d'une matrice.
- Passage : calcul autonome et interprétation correcte ; corriger ensuite soi-même l'essai argsort existant.

### M5 — Statistiques et probabilités (avant interprétation et évaluation)

- Compétences : moyenne/médiane, dispersion, biais d'échantillonnage, conditionnement.
- Intérêt : comprendre les longues durées, les jeux rares et la représentativité du dataset.
- Prérequis : M1, bases arithmétiques ; M3 pour la pratique tabulaire.
- Théorie : population/échantillon, valeurs extrêmes, fréquence et probabilité conditionnelle.
- Exercices : comparer deux distributions courtes avec et sans valeur extrême ; tableau de fréquences.
- Erreurs courantes : moyenne non pondérée de moyennes, petit effectif ignoré, corrélation interprétée comme causalité.
- Évaluation : choisir une statistique et justifier ses limites sur une situation nouvelle.
- Passage : calculer et interpréter correctement sans généralisation injustifiée.

### M6 — ML et recommandation (bases avant chaque étape, pratique ensuite)

- Compétences : baseline, feedback implicite, séparation des données, fuite, généralisation, user-user/item-item, cold start et métriques @K.
- Intérêt : savoir si un classement apporte quelque chose et pour quels utilisateurs.
- Prérequis : M3 et M5 pour baseline/évaluation ; M4 avant similarité collaborative.
- Théorie : objectif, données observées/non observées, candidats, pertinence, train/test, surapprentissage.
- Exercices : calcul manuel de Precision@K et Recall@K sur un mini-catalogue, repérer une fuite dans un protocole fictif.
- Erreurs courantes : absence d'interaction assimilée à un rejet, auto-similarité, test utilisé pour régler les paramètres.
- Évaluation : protocole expliqué avant code ; comparaison manuelle à une baseline.
- Passage : justifier population, exclusions, partition et métriques ; développer seulement l'étape dont les prérequis sont validés.

### M7 — Construction et reproductibilité (pendant développement autorisé à l'apprenant)

- Compétences : fonctions séparées, tests, paramètres, traces d'expériences et sauvegarde.
- Intérêt : refaire un résultat et localiser une erreur sans réexécuter tout le projet.
- Prérequis : M1–M3 et M6 ; M4 pour les traitements vectoriels.
- Théorie : responsabilités, effets de bord, tests de contrat, versions et traçabilité.
- Exercices : l'apprenant isole un traitement connu, écrit ses tests puis reproduit une expérience documentée.
- Erreurs courantes : lecture à l'import, dépendance cachée au notebook, test qui reproduit la même erreur que le code.
- Évaluation : cas normal et limite, reproduction avec données/paramètres/version identifiés.
- Passage : résultat reproductible expliqué et tests pertinents écrits par l'apprenant.

### M8 — Techniques avancées et mise à disposition (optionnel)

- Compétences : comparer une technique avancée justifiée, contrat d'API et contraintes d'exploitation.
- Intérêt : servir une recommandation utile après avoir démontré sa qualité.
- Prérequis : baseline évaluée, M7 et besoin explicite ; autres mathématiques à diagnostiquer selon méthode.
- Théorie : compromis qualité/coût/latence, validation des entrées, version de modèle.
- Exercices : définir un contrat fictif et expliquer une mesure de latence, puis choisir ou refuser un outil.
- Erreurs courantes : complexité sans gain, API avant évaluation, technologie choisie sans besoin.
- Évaluation : justifier le bénéfice et les limites par des observations.
- Passage : décision argumentée ; aucun déploiement ou développement automatique du mentor.

## Protocole de mise à jour

Après exercice/module significatif, noter la tentative exacte ou un résumé fidèle,
les indices donnés, erreurs, correction autonome éventuelle et preuve de validation.
Conserver l'historique, actualiser état et prochaine étape, ne jamais valider par supposition.
Relire ce fichier au début de chaque conversation. D1 est reçu : reprendre le diagnostic
Pandas P1 sans avancer vers du nouveau code métier.
