from Code.lexer import Lexer


def essai_lexer():
    monLexer = Lexer('../Exemples_programmes/test_lexer')
    for lexem in monLexer.lexems:
        print(lexem.value, lexem.kind, lexem.position)
    if len(monLexer.lexems) != 14:
        print("Erreur : le nombre de lexèmes n'est pas correct")
        return
    print("Test réussi")

if __name__ == '__main__':
    essai_lexer()
