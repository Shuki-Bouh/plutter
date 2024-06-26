from plutter.Code.lexer import Lexer
from plutter.Code.ast_project import *


class Parseur:
    """Classe qui parcourt l'ensemble des lexems pour créer l'ast et vérifier si
    le programme est conforme à la grammaire"""

    def __init__(self, file, k=0):
        self.ident = {}  # Lien entre ident et son type
        self.value_ident = {}  # Lien entre ident et sa valeur
        self.lexem = Lexer(file).lexems
        self.k = k
        return

    def show_next(self):
        return self.lexem[self.k]

    def accept(self):
        lex = self.lexem.pop(self.k)
        return lex

    def expect(self, token_kind):
        token = self.show_next()
        if token.kind == token_kind:
            lex = self.accept()
        else:
            raise TypeError("Expected ", token_kind, " got ", token.kind, " at position : ", token.position)
        return lex

    def parse_importation(self):
        imports = []
        while self.show_next().kind == 'kw_import':
            imports.append(self.parse_import())
        return Importation(imports)

    def parse_import(self):
        self.expect("kw_import")
        return Import(self.expect("ident"))

    def parse_program(self):
        self.expect("kw_figure")
        name = Name(self.expect("ident"))
        self.expect("kw_lcurbrac")
        labels = []
        declarations = []
        todraw = []
        if self.show_next().kind == 'kw_xlabel':
            labels.append(self.parse_label())
        if self.show_next().kind == 'kw_ylabel':
            labels.append(self.parse_label())
        while self.show_next().kind == 'ident':
            declarations.append(self.parse_declaration())
        while self.show_next().kind == 'kw_draw':
            todraw.append(self.parse_draw())
        self.expect('kw_rcurbrac')
        return Program(name, Labels(labels), BodyDeclaration(declarations), BodyDraw(todraw))

    def parse_label(self):
        return Label(self.accept(), self.expect('string'))

    def parse_declaration(self):
        lex = self.expect('ident')
        self.expect('kw_asign')
        value = self.parse_expression()
        self.ident[lex.value] = value.type
        self.value_ident[lex.value] = value.value
        return Declaration(lex, value)

    def parse_expression(self):

        lex = self.show_next()
        if self.is_little_expression():
            value, type_expr = self.parse_little_expression()
        elif lex.kind == 'kw_lbracket':
            self.accept()
            value = [self.parse_expression().value]
            lex = self.show_next()
            while lex.kind == 'kw_comma':
                self.accept()
                value.append(self.parse_expression().value)
                lex = self.show_next()
            self.expect('kw_rbracket')
            value = Segment(value)
            type_expr = 'segment'

        elif lex.kind == 'kw_lparenthese':
            self.accept()
            lex = self.show_next()

            if (lex.value in self.ident and
                    self.ident[lex.value] == 'distance' or
                    lex.kind == 'float'):  # Deux cas possibles : point ou cercle
                value1 = Distance(self.accept())
                self.expect('kw_comma')
                lex = self.show_next()

                if (lex.value in self.ident and
                        self.ident[lex.value] == 'distance' or
                        lex.kind == 'float'):  # C'est un point
                    value2 = Distance(self.accept())
                    type_expr = 'point'
                    value = Point(value1, value2)
                elif (lex.value in self.ident and
                      self.ident[lex.value] == 'point' or
                      lex.kind == 'kw_lparenthese'):  # C'est un cercle
                    value2 = self.parse_expression().value
                    type_expr = 'circle'
                    value = Circle(value1, value2)

                else:
                    raise TypeError("Expected ident, float or point and got ", lex.kind, " at position : ",
                                    lex.position)

            elif (lex.kind == 'kw_lparenthese' or
                  lex.value in self.ident and
                  self.ident[lex.value] == 'point'):  # C'est une droite
                value1 = self.parse_expression().value
                self.expect('kw_comma')
                if (self.show_next().kind != 'kw_lparenthese' and
                        lex.value in self.ident and
                        self.ident[lex.value] != 'point'):
                    raise TypeError("Expected '(' and got ", lex.kind, " at position : ", lex.position)
                value2 = self.parse_expression().value
                type_expr = 'droite'
                value = Droite(value1, value2)

            else:
                raise TypeError("Expected ident, float or '(' and got ", lex.kind, " at position : ", lex.position)

            self.expect('kw_rparenthese')

        else:
            raise TypeError("Expected ident, float, '[' or '(' and got ", lex.kind, " at position : ", lex.position)
        return Expression(value, type_expr)

    def parse_little_expression(self):
        lex = self.accept()
        if lex.kind == 'ident':
            if lex.value in self.ident:
                value = lex
                type_expr = self.ident[lex.value]
            else:
                raise TypeError("The variable ", lex.value, " is not declared")
        else:
            value = Distance(lex)
            type_expr = 'distance'
        return value, type_expr

    def is_little_expression(self):
        lex = self.show_next()
        if lex.kind in ['float', 'ident']:
            return True
        return False

    def parse_draw(self):
        self.expect('kw_draw')
        return Draw(self.parse_expression())

    def run(self):
        return self.parse_program()


if __name__ == '__main__':
    from Code.visitor import PrettyPrinter
    visitor = PrettyPrinter()
    pars = Parseur('../Exemples_programmes/test_compil')
    ast_prog = pars.run()
    print(ast_prog.accept(visitor))
