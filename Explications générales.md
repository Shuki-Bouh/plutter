# Le Plutter

## Introduction

Ce langage permet à un utilisateur d'afficher des figures en utilisant des notations mathématiques. 
Il est basé sur le Python et utilise la bibliothèque matplotlib pour afficher les figures.

## Installation

Pour installer le Plutter, il suffit de cloner le dépôt git suivant :

```
git clone https://github.com/Shuki-Bouh/plutter.git
```

puis d'exécuter la commande suivante :

```
pip install -r requirements.txt
```

## Utilisation

Pour utiliser le Plutter, il suffit d'utiliser la commande suivante :

```python -m plutter [path]```

où `[path]` est le chemin du fichier contenant les instructions à exécuter.

Dans un fichier code, on peut écrire des instructions pour afficher des figures :

    Point : (x, y) où x et y sont des nombres
    Segment : [(x1, y1), (x2, y2)] où x1, y1, x2 et y2 sont des nombres
    Cercle : (r, (x, y)) où x, y et r sont des nombres
    Droite : ((x1, y1), (x2, y2)) où x1, y1, x2 et y2 sont des nombres

Pour afficher ensuite une telle figure, il suffit d'utiliser la commande "draw" suivie de la figure à afficher.
En plus de cela, on peut importer un fichier avec la commande
```import [path]```
Cela permet d'importer une autre figure qu'on peut utiliser et afficher dans le code principal.