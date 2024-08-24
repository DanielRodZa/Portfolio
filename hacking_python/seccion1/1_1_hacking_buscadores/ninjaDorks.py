from dotenv import load_dotenv, set_key
import os
import argparse
import sys

from googleSearch import GoogleSearch
from duckduckgoSearch import DuckSearch
from results_parser import ResultsParser
from file_downloader import FileDownloader
from smartsearch import SmartSearch
from ia_agent import OpenAIGenerator, GPT4AllGenerator, GeminiAIGenerator, IAAgent
from browser_autosearch import BrowserAutoSearch


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

def gemini_config():
    """
    Configurar el archivo .env con los valores proporcionados para el funcionamiento de gemini
    Returns:
        None
    """
    gemini_api_key = input("Introduce tu API KEY de Gemini: ")
    set_key(".env", "GEMINI_API_KEY", gemini_api_key)

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
    while respuesta.lower() not in ("gpt", "gpt-4", "gemini", "local"):
        respuesta = input("Elige el modelo de IA a utilizar: (gpt-4/gemini/local)?: ")

    if respuesta.lower() in ("gpt", "gpt-4"):
        # Comprobamos si está definida la API KEY de OpenAI en el fichero .env
        if "OPENAI_API_KEY" not in os.environ:
            openai_config()
            load_dotenv()
        generator = OpenAIGenerator()
    elif respuesta.lower() in "gemini":
        if "GEMINI_API_KEY" not in os.environ:
            gemini_config()
            load_dotenv()
        generator = GeminiAIGenerator(API_KEY=os.environ["GEMINI_API_KEY"])
    else:
        print("Utilizando gpt4all y ejecutando la generación en local.\n"
              "Esta operación puede tomar vario minutos...")
        generator = GPT4AllGenerator()

    ia_agent = IAAgent(generator)
    respuesta = ia_agent.generate_gdork(description=gen_dork)
    print(f"\nResultado:\n{respuesta}")
    sys.exit(0)

def main_search(prompt, dir_path, max_tokens, model_name):
    if dir_path is None:
        print("Asegúrate de proporcionar una ruta de directorio para la lista de resultados.")
        sys.exit(0)

    searcher = SmartSearch(dir_path)
    resultados = searcher.ia_search(
        prompt=prompt,
        max_tokens=max_tokens,
        model_name=model_name,
    )
    for file, results in resultados.items():
        print(file)
        for r in results:
            print(f"\t-\t{r}")

def main_google(query, start_page, pages, lang, output_json, output_html, download):
    # Comprobar si existe el fichero .env
    env_exists = os.path.exists('.env')
    if not env_exists:
        print("Por favor configura las variables de entorno")
        sys.exit(1)

    # Leemos la clave API y el ID del buscador
    api_key_google = os.getenv("API_KEY_GOOGLE")
    search_engine_id = os.getenv("SEARCH_ENGINE_ID")

    if not query:
        print("Por favor introduzca una consulta con el comando -q."
              "Utiliza el comando -h para mostrar la ayuda.")
        sys.exit(1)

    gsearch = GoogleSearch(api_key_google, search_engine_id)
    results = gsearch.search(
        query=query,
        start_page=start_page,
        pages=pages,
        lang=lang
    )

    tratamiento_resultados(results, output_json, output_html)

    if download:
        file_types = download.split(",")
        urls = [resultado['link'] for resultado in results]
        fdowloader = FileDownloader("Descargas")
        fdowloader.filtro_descargas(urls, file_types)

def main_duck(query, output_json, output_html, download):
    dsearch = DuckSearch()
    results = dsearch.search(query=query)

    tratamiento_resultados(results, output_json, output_html)

    if download:
        file_types = download.split(",")
        urls = [resultado['link'] for resultado in results]
        fdowloader = FileDownloader("Descargas")
        fdowloader.filtro_descargas(urls, file_types)

def main_selenium(query, output_json, output_html):
    browser_autosearch = BrowserAutoSearch()
    browser_autosearch.search_google(query=query)
    results = browser_autosearch.google_search_results()
    tratamiento_resultados(
        resultados=results,
        fichero_json=output_json,
        fichero_html=output_html
    )


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
                             "Ej: --download 'pdf,doc,sql'"
                             "Default: 'None'")
    parser.add_argument("-gd", "--generate_dork", type=str,
                        help="Genera un dork a partir de una descripción por el usuario.\n"
                             "Ej: --generate-dork 'Listado de usuarios y passwords en ficheros de texto'")
    parser.add_argument("--smart_search", type=str,
                        help="Busca con inteligencia artificial un prompt determinado en una carpeta\n"
                             "Ej: --smart_search 'Dime los 5 puntos más importantes'")
    parser.add_argument("--dir_path", type=str, default=None,
                        help="La ruta al directorio en el que se encuentran los ficheros\n"
                             "Por defecto None")
    parser.add_argument("--model_name", type=str, default="gpt-3.5-turbo-0125",
                        help="El nombre del modelo de OpenAi para realizar la búsqueda\n"
                             "Por defecto 'gpt-3.5-turbo-0125'")
    parser.add_argument("--max_tokens", type=int, default=100,
                        help="El número máximo de tokens en la predicción\\generación.\n"
                             "Por defecto 100 tokens")
    parser.add_argument("--selenium", action='store_true', default=False,
                        help="Utiliza selenium para realizar la búsqueda con un navegador de forma automática")
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
    if args.smart_search:
        main_search(
            prompt=args.smart_search,
            dir_path=args.dir_path,
            max_tokens=args.max_tokens,
            model_name=args.model_name
        )
    if args.selenium:
        main_selenium(
            query=args.query,
            output_json=args.json,
            output_html=args.html
        )
