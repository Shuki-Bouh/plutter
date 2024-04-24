import os
from os import listdir
from os.path import isfile, join
from Code.parseur import Parseur

os.chdir("../Exemples_programmes")

class conf_pars:
    def __init__(self):
        self.valid = ['p1', 'p2', 'p3', 'p4', 'p5', 'p6', 'p7', 'p8', 'test_compil', 'test_import', 'test_import2']
        self.compil_prog()
        return

    def compil_prog(self):
        programmes = [f for f in listdir(".") if isfile(join(".", f))]
        r = 0
        i = 0
        for p in programmes:
            i += 1
            parseur = Parseur(p)
            try:
                parseur.run()

                if p in self.valid:
                    print("Test n° " + str(i) + " complété")
                    r += 1
                else:
                    print("Test n° " + str(i) + " échoué")
            except:
                if p in self.valid:
                    print("Test n° " + str(i) + " échoué")
                else:
                    print("Test n° " + str(i) + " complété")
                    r += 1

        print("Pourcentage de réussite : " + str(int(r / i * 100)) + " %")


if __name__ == '__main__':
    conf_pars()