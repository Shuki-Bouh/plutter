from Code.lexer import Lexem
from Code.plot_circle import *


class Import:
    def __init__(self, ident: Lexem):
        self.ident = ident

    def accept(self, visiteur):
        return visiteur.visite_import(self)


class Importation:
    def __init__(self, imports: list):
        self.imports = imports

    def accept(self, visiteur):
        return visiteur.visite_importation(self)


class Program:
    def __init__(self, name, declarations, to_draw):
        self.declarations = declarations
        self.to_draw = to_draw
        self.name = name
        return

    def accept(self, visiteur):
        return visiteur.visite_program(self)


class Declaration:
    def __init__(self, ident: Lexem, expr):
        self.ident = ident
        self.expr = expr

    def accept(self, visiteur):
        return visiteur.visite_declaration(self)


class LittleExpression:
    def __init__(self, value, type: str):
        self.value = value
        self.type = type

    def accept(self, visiteur):
        return visiteur.visite_little_expression(self)


class Expression:
    def __init__(self, value, type: str):
        self.value = value
        self.type = type

    def accept(self, visiteur):
        return visiteur.visite_expression(self)


class Draw:
    def __init__(self, expr: Expression):
        self.expr = expr

    def accept(self, visiteur):
        return visiteur.visite_draw(self)


class BodyDraw:
    def __init__(self, to_draw: list):
        self.to_draw = to_draw

    def accept(self, visiteur):
        return visiteur.visite_body_draw(self)


class Name:
    def __init__(self, name: Lexem):
        self.name = name

    def accept(self, visiteur):
        return visiteur.visite_name(self)


class BodyDeclaration:
    def __init__(self, declarations: list):
        self.declarations = declarations

    def accept(self, visiteur):
        return visiteur.visite_body_declaration(self)


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def accept(self, visiteur):
        return visiteur.visite_point(self)

    def draw(self, compilator):
        compilator.ax.plot(self.x.draw(compilator), self.y.draw(compilator), 'ro')
        return


class Circle:
    def __init__(self, radius, center):
        self.center = center
        self.radius = radius

    def accept(self, visiteur):
        return visiteur.visite_circle(self)

    def draw(self, compilator):
        X, Y = create_circle((self.center.x.draw(compilator), self.center.y.draw(compilator)),
                             self.radius.draw(compilator))

        compilator.ax.plot(X, Y, 'r')
        return


class Droite:
    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2

    def accept(self, visiteur):
        return visiteur.visite_droite(self)

    def draw(self, compilator):
        compilator.ax.plot([self.point1.x.draw(compilator), self.point2.x.draw(compilator)],
                           [self.point1.y.draw(compilator), self.point2.y.draw(compilator)], 'r')
        return


class Segment:
    def __init__(self, point: list):
        self.point = point

    def accept(self, visiteur):
        return visiteur.visite_segment(self)

    def draw(self, compilator):
        for i in range(len(self.point)-1):
            compilator.ax.plot([self.point[i].x.draw(compilator), self.point[i+1].x.draw(compilator)],
                               [self.point[i].y.draw(compilator), self.point[i+1].y.draw(compilator)], 'r')
        return


class Distance:
    def __init__(self, value):
        self.value = value

    def accept(self, visiteur):
        return visiteur.visite_distance(self)

    def draw(self, compilator):
        return self.value.draw(compilator)



