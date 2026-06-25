# Rock-Paper-Scissors Mini Project

## Description
Ce mini-projet implémente un jeu de Pierre-Papier-Ciseaux en Python.
Le programme permet à l'utilisateur de jouer plusieurs manches contre l'ordinateur, d'afficher le score et de quitter le jeu.

## Fichiers
- `game.py` : contient la classe `Game` avec la logique du jeu.
- `rock-paper-scissors.py` : script principal qui affiche le menu, lance les parties et suit les scores.

## Fonctionnement
1. Le joueur choisit une action dans le menu principal :
   - 1 : jouer une nouvelle partie
   - 2 : afficher les scores
   - 3 : quitter le jeu
2. Lors d'une partie, le joueur choisit `(r)` pour rock, `(p)` pour paper ou `(s)` pour scissors.
3. L'ordinateur choisit aléatoirement une option parmi `r`, `p`, `s`.
4. Le résultat est calculé et affiché : victoire, défaite ou égalité.
5. Les scores cumulés sont mis à jour pour chaque partie jouée.

## Fonctionnalités
- Menu interactif en ligne de commande.
- Saisie contrôlée pour le choix du joueur.
- Choix aléatoire de l'ordinateur.
- Calcul du résultat selon les règles classiques du jeu.
- Conservation et affichage des scores cumulés : victoires, défaites, égalités.

## Utilisation
Exécutez le script principal :

```bash
python rock-paper-scissors.py
```

Puis suivez les instructions à l'écran.

## Remarques
- Le score est conservé uniquement pendant l'exécution du programme.
- Une validation de saisie plus robuste peut être ajoutée pour éviter les erreurs lorsque l'utilisateur entre une valeur non numérique dans le menu.
