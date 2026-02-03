# Morpion (Tic-Tac-Toe)

Ce projet est une implémentation complète du jeu du **Morpion** en Python, jouable directement dans le terminal.  
Il propose plusieurs modes, une gestion du temps pour les tours du joueur, une IA stratégique simple et une structure de code propre et documentée.

---
## Fonctionnalités

### Mode 2 joueurs
Deux joueurs humains s'affrontent au tour par tour.

### IA aléatoire
L'ordinateur joue un coup valide choisi au hasard.

### IA stratégique
Une intelligence artificielle capable de :
- jouer un coup gagnant si disponible
- bloquer un coup gagnant adverse
- sinon jouer aléatoirement

### Limite de temps pour jouer
Le joueur dispose d’un temps défini (par défaut 10 secondes) pour entrer :
- la ligne  
- la colonne  

Si le temps est écoulé :
- un coup automatique est joué par l’ordinateur

---
## Structure du projet

```
morpion/
├── morpion.py             # Script principal du jeu
└── (évolutif : modules, assets, GUI, etc.)
```

---
## Lancer le jeu

Dans un terminal :

```bash
python morpion.py
```

Le jeu affiche ensuite le menu :

```
=== MORPION ===
Modes :
1. 2 joueurs
2. IA aléatoire
3. IA stratégique
```

---

##  Aperçu du gameplay

- Le plateau est affiché après chaque coup.
- Les cases vides sont représentées par `-`.
- Le joueur `X` commence toujours.
- Le jeu détecte :
  - victoire en ligne
  - victoire en colonne
  - victoire diagonale
  - match nul

---
## Technologies

- Python 3
- Modules standards : `random`, `time`

Aucune installation externe requise.

--- 
## 📄 Licence

MIT License.
