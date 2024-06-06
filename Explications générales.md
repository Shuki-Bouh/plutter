# Le Plutter

## Introduction

Ce langage permet à un utilisateur d'afficher des figures en utilisant des notations mathématiques. 
Il est basé sur le Python et utilise la bibliothèque matplotlib pour afficher les figures.

## Installation

Pour installer le Plutter, il suffit de cloner le dépôt git suivant :

```
git clone https://github.com/Shuki-Bouh/plutter.git
```

puis en vous placant dans le répertoire plutter, exécutez la commande shell suivante :

```
pip install -r requirements.txt
```

## Utilisation

Pour exécuter un script Plutter, vous devez vous placer dans le répertoire où plutter est clone (et non pas dans le 
répertoire plutter). Exemple : si le dossier plutter se trouve dans Downloads, veuillez vous placer dans Downloads puis exécutez :

```python -m plutter [path]```

où `[path]` est le code source de votre programme principal. Si vous importez des figures, ces figures doivent se 
trouver dans le même répertoire que votre code principal. `[path]` peut être un chemin absolu ou relatif.



Dans un fichier code, on peut écrire des instructions pour afficher des figures :

    Point : (x, y) où x et y sont des nombres
    Segment : [point (, point)*]
    Cercle : (r, point) où et r sont des nombres
    Droite : (point1, point2) 

Pour afficher ensuite une telle figure, il suffit d'utiliser la commande ```draw``` suivie de la figure à afficher.
En plus de cela, on peut importer un fichier avec la commande
```ìmport [file]``` `[file]` étant un fichier dans le même répertoire que le code source.
Cela permet d'importer une autre figure qu'on peut utiliser et afficher dans le code principal.

## Grammaire

```
Import : (import ident)*
figure : figue ident { label* declaration* draw* }
label : xlabel string | ylabel string
declaration : DistanceDecl | PointDecl | SegmentDecl | CercleDecl | DroiteDecl
DistanceDecle : ident = little_expr
PointDecl : ident = (little_expr, little_expr)
SegmentDecl : ident = [Point (, Point)*]
CercleDecl : ident = (little_expr, Point)
DroiteDecl : ident = (Point, Point)
little_expr : float | ident
```

## Figure imposée

**Lexer** : lexer du TD légèrement modifié pour qu'il corresponde au langage

**Parser** : parser dédié à ce code pour prendre en compte facilement le non typage des variables

**Ast** : Est généré par le compilateur avec une méthode accept pour les deux visiteurs ....

**Visiteur** :
    Un pretty_printer est généré avec le patern visiteur
    Un autre visiteur est créé par le compilateur pour afficher les figures : DrawVisitor

## Remarques :

 - Il est possible d'écrire des commentaires avec // ou /* */
 - Un certain nombre de programmes test sont disponibles dans le dossier Exemples Programmes pour voir les fonctionnalités du langage
