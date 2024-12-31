import argparse
import zipfile
from Descompresor import Descompresor

def main():
    """
    Función principal
    """

    parser = argparse.ArgumentParser(description='Descomprime archivos Zip')
    parser.add_argument('file', help='archivo .zip')
    parser.add_argument('-d', '--destino', help='Descomprime archivo .zip')

    args = parser.parse_args()

    descomprimir = Descompresor(args.file, args.destino)

    try:
        descomprimir.descomprimir()
    except (FileNotFoundError, zipfile.BadZipFile) as e:
        print(e)

if __name__ == '__main__':
    main()