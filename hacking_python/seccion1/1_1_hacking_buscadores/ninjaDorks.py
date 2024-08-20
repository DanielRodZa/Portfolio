from dotenv import load_dotenv, set_key
import os
import argparse
import sys

from googleSearch import GoogleSearch
from duckduckgoSearch import DuckSearch
from results_parser import ResultsParser
from file_downloader import FileDownloader
from ia_agent import OpenAIGenerator, GPT4AllGenerator, IAAgent


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


def openai_config():
    """
    Configurar el archivo .env con los valores proporcionados para el funcionamiento de openai
    Returns:
        None
    """
    openai_api_key = input("Introduce tu API KEY de Open AI: ")
    set_key(".env", "OPENAI_API_KEY", openai_api_key)


def tratamiento_resultados(resultados, fichero_json=None, fichero_html=None):
    # Crea y muestra los resultados por consola
    result_processor = ResultsParser(resultados=resultados)
    result_processor.mostrar_pantalla()

    # Comprueba que se haya pedido un json o un html
    if fichero_json is not None:
        result_processor.exportar_json(fichero_json)
    if fichero_html is not None:
        result_processor.exportar_html(fichero_html)

def generate_dork(gen_dork):
    # Preguntar si el usuario quiere usar un modelo local u OpenAI
    respuesta = ""
    while respuesta.lower() not in ("y", "yes", "n", "no"):
        respuesta = input("Quieres utilizar GPT-4 de OpenAi: (yes/no)?: ")

    if respuesta.lower() in ("y", "yes"):
        # Comprobamos si esta definida la API KEY de Opena AI en el fichero .env
        if not "OPENAI_API_KEY" in os.environ:
            openai_config()
            load_dotenv()
        openai_generator = OpenAIGenerator()
        ia_agent = IAAgent(openai_generator)
    else:
        print("Utilizando gpt4all y ejecutando la generación en local.\n"
              "Esta operación puede tomar vario minutos...")
        gpt4all_generator = GPT4AllGenerator()
        ia_agent = IAAgent(gpt4all_generator)

    respuesta = ia_agent.generate_gdork(description=gen_dork)
    print(f"\nResultado:\n{respuesta}")
    sys.exit(0)

def main_google(query, start_page, pages, lang, output_json, output_html, download):
    # Comprobar si existe el fichero .env
    env_exists = os.path.exists('.env')
    if not env_exists:
        print("Por favor configura las variables de entorno")
        sys.exit(1)

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

    tratamiento_resultados(results, output_json, output_html)

    if download:
        file_tipes = download.split(",")
        urls = [resultado['link'] for resultado in results]
        fdowloader = FileDownloader("Descargas")
        fdowloader.filtro_descargas(urls, file_tipes)


def main_duck(query, output_json, output_html, download):
    dsearch = DuckSearch()
    results = dsearch.search(query=query)

    tratamiento_resultados(results, output_json, output_html)

    if download:
        file_tipes = download.split(",")
        urls = [resultado['link'] for resultado in results]
        fdowloader = FileDownloader("Descargas")
        fdowloader.filtro_descargas(urls, file_tipes)


if __name__ == '__main__':
    # Cargamos las variables de entorno
    load_dotenv()
    # Configuración de los argumentos del programa
    parser = argparse.ArgumentParser(description='Esta herramienta permite hacer '
                                                 'queries en buscadores de forma '
                                                 'automática')
    parser.add_argument('-q', '--query',
                        help='Especifica el dork que desea buscar\nEjemplo: '
                             '-q \'filetype:sql "MySQL dump" (pass|password|psswd|pwd)\'', )
    parser.add_argument('-c', '--configure', action='store_true',
                        help='Inicia el proceso de configuración del archivo .env\nUtiliza '
                             'esta opción sin otros argumentos para configurar las claves')
    parser.add_argument('--start_page', type=int, default=1,
                        help='Define la página de inicio del buscador')
    parser.add_argument("--pages", type=int, default=1,
                        help='Número de páginas de resultados de búsqueda')
    parser.add_argument("--lang", type=str, default='lang_es',
                        help='Código de idioma para los resultados.\nDefault: "lang_es"')
    parser.add_argument('-g', '--google', action='store_true', )
    parser.add_argument('-d', '--duck', action='store_true', )
    parser.add_argument('--json', type=str,
                        help='Exporta los resultado en formato json')
    parser.add_argument('--html', type=str,
                        help='Exporta los resultado en formato html')
    parser.add_argument('--download', type=str, default='all',
                        help="Especifica las extensiones de los archivos que quieres descargar separadas por coma."
                             "Ej: --dowload 'pdf,doc,sql'"
                             "Default: 'None'")
    parser.add_argument("-gd", "--generate_dork", type=str,
                        help="Genera un dork a partir de una descripción por el usuario.\n"
                             "Ej: --generate-dork 'Listado de usuarios y passwords en ficheros de texto'")
    args = parser.parse_args()
    if args.configure:
        env_config()
        print("Archivo .env configurado satisfactoriamente")
        sys.exit(1)
    if args.generate_dork:
        generate_dork(
            gen_dork=args.generate_dork,
        )
    if args.google:
        main_google(
            query=args.query,
            start_page=args.start_page,
            pages=args.pages,
            lang=args.lang,
            output_json=args.json,
            output_html=args.html,
            download=args.download
        )
    if args.duck:
        main_duck(
            query=args.query,
            output_json=args.json,
            output_html=args.html,
            download=args.download
        )
