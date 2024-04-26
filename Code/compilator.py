from Code.parseur import Parseur
from Code.visitor import *
import matplotlib.pyplot as plt
from Code.ast_project import AST


class Compile:
    def __init__(self):
        return

    @staticmethod
    def run(compilator):
        file_to_import = compilator.importation()
        for file in file_to_import.imports:
            imported = CompilatorWithoutDraw(file.ident.value)
            imported.compile()
            # On place dans le dictionnaire de l'ast principal les ident et leurs valeurs des figures importées
            compilator.parseur.ident.update(imported.parseur.ident)
            compilator.parseur.value_ident.update(imported.parseur.value_ident)
        print(compilator.gen_ast())  # On affiche le pretty print de l'ast


class CompilatorWithoutDraw:
    """Cette classe permet de gérer les importations. Dans ce langage les importations ne servent qu'à déclarer une
    figure sans la tracer. Si on veut la tracer, il faut la tracer dans la figure principale"""

    def __init__(self, file):
        self.parseur = Parseur(file)
        self.pretty_printer = PrettyPrinter()
        return

    def importation(self):
        return self.parseur.parse_importation()

    def gen_ast(self):
        self.ast = self.parseur.run()
        return self.pretty_printer.visite_program(self.ast)

    def compile(self):
        Compile.run(self)  # Patern stratégie
        return


class Compilator:
    """Cette classe permet de compiler une figure et la tracer. Elle gère les importations et les tracés de figures"""

    def __init__(self, file):
        self.parseur = Parseur(file)
        self.pretty_printer= PrettyPrinter()
        self.draw_visitor = DrawVisitor(self)
        self.ast = AST()
        self.fig = plt.figure()
        self.ax = self.fig.add_subplot(111)
        plt.axis('equal')
        return

    def importation(self):
        self.ast.importation = self.parseur.initialize()
        return self.ast.importation

    def gen_ast(self):
        self.ast.program = self.parseur.run()
        return self.pretty_printer.visite_ast(self.ast)

    def compile(self):
        Compile.run(self)
        self.draw_visitor.visite_ast(self.ast)
        return

    @staticmethod
    def draw(file):
        compilator = Compilator(file)
        compilator.compile()
        plt.show()


if __name__ == '__main__':
    import os
    os.chdir("../Exemples_programmes")
    Compilator.draw("test_compil")