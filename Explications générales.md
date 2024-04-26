# Le Plutter

## Introduction

Ce langage permet à un utilisateur d'afficher des figures en utilisant des notations mathématiques. 
Il est basé sur le Python et utilise la bibliothèque matplotlib pour afficher les figures.

## Installation

Pour installer le Plutter, il suffit de cloner le dépôt git suivant :

```
git clone https://github.com/Shuki-Bouh/plutter.git
```

puis d'exécuter la commande shell suivante :

```
pip install -r requirements.txt
```

## Utilisation

Pour exécuter un script Plutter, il suffit d'utiliser la commande suivante :

```python -m plutter [path]```

où `[path]` est le chemin du fichier contenant les instructions à exécuter.

Dans un fichier code, on peut écrire des instructions pour afficher des figures :

    Point : (x, y) où x et y sont des nombres
    Segment : [point (, point)*]
    Cercle : (r, point) où et r sont des nombres
    Droite : (point1, point2) 

Pour afficher ensuite une telle figure, il suffit d'utiliser la commande ```draw``` suivie de la figure à afficher.
En plus de cela, on peut importer un fichier avec la commande
```import [path]``` ou ```ìmport [file]``` si le fichier à importer se trouve dans le même répertoire que le fichier principal.
Cela permet d'importer une autre figure qu'on peut utiliser et afficher dans le code principal.

## Figure imposée

**Lexer** : lexer du TD légèrement modifié pour qu'il corresponde au langage

**Parser** : parser dédié à ce code pour prendre en compte facilement le non typage des variables

**Ast** : Est généré par le compilateur avec une méthode accept pour les deux visiteurs ....

**Visiteur** :
    Un pretty_printer est généré avec le patern visiteur
    Un autre visiteur est créé par le compilateur pour afficher les figures : DrawVisitor

**Stratégie**
    Une classe Compile est ajoutée pour mettre en place un patern stratégie
    -> La méthode compile dans Compilator et CompilatorWithoutDraw est modifiée dans Compile 
pour éviter les trop nombreuses modifications de code