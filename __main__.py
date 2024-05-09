from plutter.Code.compilator import Compilator
import sys
import os

if __name__ == '__main__':

    if len(sys.argv) == 2:
        folder = sys.argv[1].split('/')
        file = folder.pop()
        folder = '/'.join(folder)
        os.chdir(folder)
        Compilator.draw(file)
