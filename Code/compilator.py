from plutter.Code.parseur import Parseur
from plutter.Code.visitor import *
import matplotlib.pyplot as plt
from plutter.Code.ast_project import AST


class CompileWithoutDrawing:
    def __init__(self, file):
        self.parseur = Parseur(file)
        self.pretty_printer = PrettyPrinter()
        self.draw_visitor = DrawVisitor(self)
        self.ast = AST()
        return

    def importation(self):
        self.ast.importation = self.parseur.parse_importation()
        return self.ast.importation

    def gen_ast(self):
        self.ast.program = self.parseur.run()
        return self.pretty_printer.visite_ast(self.ast)

    def compile(self):
        file_to_import = self.importation()
        for file in file_to_import.imports:
            imported = CompileWithoutDrawing(file.ident.value)  # On compile le fichier importé
            imported.compile()
            # On place dans le dictionnaire de l'ast principal les ident et leurs valeurs des figures importées
            self.parseur.ident.update(imported.parseur.ident)
            self.parseur.value_ident.update(imported.parseur.value_ident)
        print(self.gen_ast())  # On affiche le pretty print de l'ast


class Compilator(CompileWithoutDrawing):
    """Cette classe permet de compiler une figure et la tracer. Elle gère les importations et les tracés de figures"""

    def __init__(self, file):
        super().__init__(file)
        self.ast = AST()
        self.fig = plt.figure()
        self.ax = self.fig.add_subplot(111)
        plt.axis('equal')
        return

    def compile(self):
        super().compile()  # Patern Strategy
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
    Compilator.draw("test_overwrite")
