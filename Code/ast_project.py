from Code.lexer import Lexem


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


class Name:
    def __init__(self, name: Lexem):
        self.name = name

    def accept(self, visiteur):
        return visiteur.visite_name(self)


class LittleExpression:
    def __init__(self, value, type_lex: str):
        self.value = value
        self.type = type_lex

    def accept(self, visiteur):
        return visiteur.visite_little_expression(self)


class Expression:
    def __init__(self, value, type_obj: str):
        self.value = value
        self.type = type_obj

    def accept(self, visiteur):
        return visiteur.visite_expression(self)


class Declaration:
    def __init__(self, ident: Lexem, expr):
        self.ident = ident
        self.expr = expr

    def accept(self, visiteur):
        return visiteur.visite_declaration(self)


class BodyDeclaration:
    def __init__(self, declarations: list):
        self.declarations = declarations

    def accept(self, visiteur):
        return visiteur.visite_body_declaration(self)


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


class Label:
    def __init__(self, ident: Lexem, name: Lexem):
        self.ident = ident
        self.name = name

    def accept(self, visiteur):
        return visiteur.visite_label(self)


class Labels:
    def __init__(self, labels: list):
        self.labels = labels

    def accept(self, visiteur):
        return visiteur.visite_labels(self)


class Program:
    def __init__(self, name: Name, labels: Labels, declarations: BodyDeclaration, to_draw: BodyDraw):
        self.labels = labels
        self.declarations = declarations
        self.to_draw = to_draw
        self.name = name
        return

    def accept(self, visiteur):
        return visiteur.visite_program(self)


class AST:
    def __init__(self):
        self.importation: Importation = None
        self.program: Program = None

    def accept(self, visiteur):
        return visiteur.visite_ast(self)


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def accept(self, visiteur):
        return visiteur.visite_point(self)


class Circle:
    def __init__(self, radius, center):
        self.center = center
        self.radius = radius

    def accept(self, visiteur):
        return visiteur.visite_circle(self)


class Droite:
    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2

    def accept(self, visiteur):
        return visiteur.visite_droite(self)


class Segment:
    def __init__(self, point: list):
        self.point = point

    def accept(self, visiteur):
        return visiteur.visite_segment(self)


class Distance:
    def __init__(self, value):
        self.value = value

    def accept(self, visiteur):
        return visiteur.visite_distance(self)
