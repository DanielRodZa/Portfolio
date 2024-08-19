from dotenv import load_dotenv, set_key
import os
import argparse
import sys

from googleSearch import GoogleSearch
from duckduckgoSearch import DuckSearch


def env_config():
    """
    Configurar el archivo .env con los valores proporcionados
    Returns:
        None
    """
    api_key = input("Introduce tu API KEY: ")
    engine_id = input("Introduce tu engine ID: ")
    set_key(".env", "API_KEY_GOOGLE", api_key)
    set_key(".env", "SEARCH_ENGINE_ID", engine_id)


def main_google(query, start_page, pages, lang):
    # Comprobar si existe el fichero .env
    env_exists = os.path.exists('.env')
    if not env_exists:
        print("Por favor configura las variables de entorno")
        sys.exit(1)

    # Cargamos las variables de entorno
    load_dotenv()

    # Leemos la clave API y el ID del buscador
    API_KEY_GOOGLE = os.getenv("API_KEY_GOOGLE")
    SEARCH_ENGINE_ID = os.getenv("SEARCH_ENGINE_ID")

    if not query:
        print("Por favor introduzca una consulta con el comando -q."
              "Utiliza el comando -h para mostrar la ayuda.")
        sys.exit(1)

    gsearch = GoogleSearch(API_KEY_GOOGLE, SEARCH_ENGINE_ID)
    results = gsearch.search(
        query=query,
        start_page=start_page,
        pages=pages,
        lang=lang
    )

    for r in results:
        print(r)

def main_duck(query):
    dsearch = DuckSearch()
    results = dsearch.search(query=query)

    for r in results:
        print(r)


if __name__ == '__main__':
    # Configuración de los argumentos del programa
    parser = argparse.ArgumentParser(description='Esta herramienta permite hacer '
                                                 'queries en buscadores de forma '
                                                 'automática')
    parser.add_argument('-q','--query',
                        help='Especifica el dork que desea buscar\nEjemplo: '
                             '-q \'filetype:sql "MySQL dump" (pass|password|psswd|pwd)\'',)
    parser.add_argument('-c','--configure', action='store_true',
                        help='Inicia el proceso de configuración del archivo .env\nUtiliza '
                             'esta opción sin otros argumentos para configurar las claves')
    parser.add_argument('--start_page', type=int, default=1,
                        help='Define la página de inicio del buscador')
    parser.add_argument("--pages", type=int, default=1,
                        help='Número de páginas de resultados de búsqueda')
    parser.add_argument("--lang", type=str, default='lang_es',
                        help='Código de idioma para los resultados.\nDefault: "lang_es"')
    parser.add_argument('-g', '--google', action='store_true',)
    parser.add_argument('-d', '--duck', action='store_true',)
    args = parser.parse_args()
    if args.configure:
        env_config()
        print("Archivo .env configurado satisfactoriamente")
        sys.exit(1)

    if args.google:
        main_google(
            query=args.query,
            start_page=args.start_page,
            pages=args.pages,
            lang=args.lang
        )
    if args.duck:
        main_duck(
            query=args.query
        )
