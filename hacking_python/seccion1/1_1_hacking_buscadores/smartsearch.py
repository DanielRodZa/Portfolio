import os
import re
import argparse


class SmartSearch:
    """
    Smart Search Class
    Ayuda a buscar un patrón creado por una expresión regular en una carpeta o fichero
    """
    def __init__(self, dir_path):
        self.dir_path = dir_path
        self.files = self._read_files()

    def _read_files(self):
        """
        Esto lee el contenido de los ficheros que se encuentran en un directorio
        Returns:
            None
        """
        files = {}
        # Listar los ficheros del directorio
        for archivo in os.listdir(self.dir_path):
            file_path = os.path.join(self.dir_path, archivo)
            try:
                with open(file_path, mode='r', encoding='utf-8') as file:
                    files[archivo] = file.read()
            except Exception as e:
                print(f"Error al leer el archivo {file_path}:\nERROR: {e}")
        return files

    def regex_search(self, regex):
        """
        Busca información utilizando expresiones regulares
        Args:
            regex :

        Returns:

        """
        coincidencias = {}
        # Recorremos el contenid de todos los ficeros del directorio
        for file, text in self.files.items():
            respuesta = ""
            while respuesta not in ("y", "n", "yes", "no"):
                respuesta = input(f"El fichero {file} tiene una longitud de {len(text)} caracteres\n"
                                  f"¿Quieres procesarlo? (yes/no)")
                if respuesta in ("no", "n"):
                    continue
                matches = re.findall(regex, text, re.IGNORECASE)
                if not matches == []:
                    coincidencias[file] = matches
        return coincidencias

if __name__ == "__main__":
    # Configuramos los argumentos del programa
    parser = argparse.ArgumentParser(
        description="Smart Search:\n"
                    "Esta herramienta realiza búsquedas en los ficheros de un directorio"
    )
    parser.add_argument("dir_path", type=str,
                        help="La ruta al directorio en el que se encuentran los ficheros")
    parser.add_argument("-r","--regex", type=str,
                        help="La expresión regular para realizar la búsqueda")

    # Parseamos los argumentos
    args = parser.parse_args()
    if args.regex:
        searcher = SmartSearch(args.dir_path)
        resultados = searcher.regex_search(args.regex)
        for file, results in resultados.items():
            print(file)
            for r in results:
                print(f"\t-\t{r}")