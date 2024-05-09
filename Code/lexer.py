class Lexem:
    def __init__(self, kind: str, value: str, position: tuple):
        self.kind = kind
        self.value = value
        self.position = position

    def accept(self, visiteur):
        return visiteur.visite_lexem(self)


class Lexer:
    """Créer une liste de lexems à partir d'un fichier"""

    regex = {
        r'import': 'kw_import',
        r'figure': 'kw_figure',
        r'draw': 'kw_draw',
        r'xlabel': 'kw_xlabel',
        r'ylabel': 'kw_ylabel',
        r'(': 'kw_lparenthese',
        r')': 'kw_rparenthese',
        r'{': 'kw_lcurbrac',
        r'}': 'kw_rcurbrac',
        r'[': 'kw_lbracket',
        r']': 'kw_rbracket',
        r'=': 'kw_asign',
        r',': 'kw_comma',
    }

    def __init__(self, file):
        self.lexems = []
        self.run(file)
        return

    @staticmethod
    def find_type(word):
        try:
            type_lex = Lexer.regex[word]
        except KeyError:
            try:
                float(word)
                type_lex = 'float'
            except ValueError:
                type_lex = 'ident'
        return type_lex

    def process(self, data):
        is_str = False
        is_comment = False
        temp = []
        for row in range(len(data)):
            data[row] = list(data[row])  # On convertit la chaine de caractère en liste : "bonjour" ->
            # ['b', 'o', ...] pour travailler caractère par caractère
            col = 0
            position = (row, col)  # On initialise la position pour chaque ligne
            while col < len(data[row]):
                if "".join(temp) == '//':
                    temp = []
                    break
                elif "".join(temp) == '/*':
                    is_comment = True
                    temp = []
                elif '*/' in "".join(temp):
                    temp = []
                    is_comment = False
                elif is_comment:
                    temp.append(data[row][col])
                elif is_str:
                    if data[row][col] == '"':
                        is_str = False
                        valeur = "".join(temp)
                        kind = 'string'
                        self.lexems.append(Lexem(kind, valeur, position))
                        temp = []
                    elif data[row][col] == '\n':
                        raise TypeError("Erreur : fin de ligne avant la fin de la chaine de caractère")
                    else:
                        temp.append(data[row][col])

                else:
                    if data[row][col] == '\n':  # fin de ligne
                        if temp:  # Si on a un mot en cours de lecture, on l'ajoute à la liste des lexems
                            valeur = "".join(temp)
                            kind = self.find_type(valeur)
                            self.lexems.append(Lexem(kind, valeur, position))
                            temp = []
                        else:
                            break  # On passe à la ligne suivante
                    else:
                        if "".join(temp) in Lexer.regex:  # On vérifie que le mot en cours de lecture n'est pas un regex
                            value = "".join(temp)  # Si c'est le cas, on l'ajoute à la liste des lexems
                            kind = Lexer.regex[value]
                            self.lexems.append(Lexem(kind, value, position))
                            position = (row, col)
                            temp = []

                        if data[row][col] == ' ' or data[row][col] == '\t':
                            # Dans le cas d'un espace, on voit apparaitre un nouveau lexem
                            if temp:
                                valeur = "".join(temp)
                                kind = self.find_type(valeur)
                                self.lexems.append(Lexem(kind, valeur, position))
                                temp = []
                            position = (row, col + 1)

                        elif data[row][col] in Lexer.regex:
                            # Un autre cas où on doit interrompre notre
                            # lexem est le cas où un caractère régulier apparait
                            if temp:
                                valeur = "".join(temp)
                                kind = self.find_type(valeur)
                                self.lexems.append(Lexem(kind, valeur, position))
                                temp = []
                                position = (row, col)
                            self.lexems.append(Lexem(Lexer.regex[data[row][col]], data[row][col], position))
                            position = (row, col + 1)

                        elif col == len(data[row]) - 1:  # Dernier cas barbare : fin de ligne sans \n
                            temp.append(data[row][col])
                            valeur = "".join(temp)
                            kind = self.find_type(valeur)
                            self.lexems.append(Lexem(kind, valeur, position))
                            temp = []

                        elif data[row][col] == '"':  # On commence une chaine de caractère
                            is_str = True
                            if temp:
                                valeur = "".join(temp)
                                kind = self.find_type(valeur)
                                self.lexems.append(Lexem(kind, valeur, position))
                                temp = []
                            position = (row, col)

                        else:  # Autrement on continue notre route comme si de rien n'était
                            temp.append(data[row][col])
                col += 1
            row += 1

    def run(self, file):
        with open(file) as prog:
            data = prog.readlines()  # On a récupéré les données du fichier
        self.process(data)


if __name__ == '__main__':
    lexem = Lexer('../Exemples_programmes/test_import')
    for lex in lexem.lexems:
        print(lex.value)
