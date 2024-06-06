from plutter.Code.compilator import Compilator
import sys
import os
import argparse


def main():
    parser = argparse.ArgumentParser(description="Traitement d'un fichier donné en argument")
    parser.add_argument('filename', type=str, help='Le chemin vers le fichier à traiter')

    args = parser.parse_args()
    filename= args.filename
    directory = os.path.dirname(filename)
    print(directory)

    try:
        file = open(filename, 'r')
        file.close()
    except FileNotFoundError:
        print(f"Erreur : Le fichier {args.filename} n'a pas été trouvé.")
        sys.exit(1)
    except Exception as e:
        print(f"Une erreur est survenue lors de la lecture du fichier: {e}")
        sys.exit(2)
    try:
        os.chdir(directory)
    except OSError:
        pass
    Compilator.draw(filename)

if __name__ == "__main__":
    main()
