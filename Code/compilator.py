from Code.parseur import Parseur
from Code.visitor import *
import matplotlib.pyplot as plt


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
        file_to_import = self.importation()
        for file in file_to_import.imports:
            compilator = Compilator(file.ident.value)
            compilator.compile()
            self.parseur.ident.update(compilator.parseur.ident)
            self.parseur.value_ident.update(compilator.parseur.value_ident)
        print(self.gen_ast())
        return


class Compilator:
    """Cette classe permet de compiler une figure et la tracer. Elle gère les importations et les tracés de figures"""

    def __init__(self, file):
        self.parseur = Parseur(file)
        self.pretty_printer= PrettyPrinter()
        self.draw_visitor = DrawVisitor(self)
        self.ast = None
        self.fig = plt.figure()
        self.ax = self.fig.add_subplot(111)
        plt.axis('equal')
        return

    def importation(self):
        return self.parseur.initialize()

    def gen_ast(self):
        self.ast = self.parseur.run()
        return self.pretty_printer.visite_program(self.ast)

    def compile(self):

        # Partie dédiée à l'importation
        file_to_import = self.importation()
        for file in file_to_import.imports:
            compilator = CompilatorWithoutDraw(file.ident.value)
            compilator.compile()
            # On place dans le dictionnaire de l'ast principal les ident et leurs valeurs des figures importées
            self.parseur.ident.update(compilator.parseur.ident)
            self.parseur.value_ident.update(compilator.parseur.value_ident)

        print(self.gen_ast())  # On affiche le pretty print de l'ast

        self.drawing()  # On trace les figures
        return

    def drawing(self):
        self.ax.title.set_text(self.ast.name.name.value)  # On nomme la figure
        to_draw = self.ast.to_draw.to_draw  # On récupère les figures à tracer (c'est une liste
        for draw in to_draw:
            draw.expr.value.accept(self.draw_visitor)

    @staticmethod
    def draw(file):
        compilator = Compilator(file)
        compilator.compile()
        plt.show()


if __name__ == '__main__':
    import os
    os.chdir("../Exemples_programmes")
    Compilator.draw("test_compil")