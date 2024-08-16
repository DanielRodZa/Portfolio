from dotenv import load_dotenv
import os
import argparse

from googleSearch import GoogleSearch
from duckduckgoSearch import DuckSearch

# Cargamos las variables de entorno
load_dotenv()

# Leemos la clave API (MAX. 10 PETICIONES)
API_KEY_GOOGLE = os.getenv("API_KEY_GOOGLE")

# Leemos el indentificador
SEARCH_ENGINE_ID = os.getenv("SEARCH_ENGINE_ID")

query = ''

def main_google():
    gsearch = GoogleSearch(API_KEY_GOOGLE, SEARCH_ENGINE_ID)
    results = gsearch.search(query=query)

    print(results)

def main_duck():
    dsearch = DuckSearch()
    results = dsearch.search(query=query)

    print(results)

if __name__ == '__main__':
    # Configuración de los argumentos del programa
    parser = argparse.ArgumentParser(description='Esta herramienta permite hacer '
                                                 'queries en buscadores de forma '
                                                 'automática')
    parser.add_argument('-q','--query',
                        help='Especifica el dork que desea buscar\nEjemplo: '
                             '-q \'filetype:sql "MySQL dump" (pass|password|psswd|pwd)\'',)
    parser.add_argument('-c','--configure', action='store_true',
                        help='Inicia el proceso de configuracion del archivo .env\nUtiliza '
                             'esta opción sin otros argumentos para configurar las claves')
    parser.add_argument('--start-page', type=int, default=1,
                        help='Define la página de inicio del buscador')
    parser.add_argument("--pages", type=int, default=1,
                        help='Número de páginas de resultados de búsqueda')
    parser.add_argument("--lang", type=str, default='lang_es',
                        help='Código de idioma para los resultados.\nDefault: "lang_es"')
    parser.add_argument('-g', '--google', action='store_true',)
    parser.add_argument('-d', '--duck', action='store_true',)
    args = parser.parse_args()
    main_google()
