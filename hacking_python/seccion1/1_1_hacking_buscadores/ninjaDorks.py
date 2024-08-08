from dotenv import load_dotenv
import os

from googleSearch import GoogleSearch
from duckduckgoSearch import DuckSearch

# Cargamos las variables de entorno
load_dotenv()

# Leemos la clave API (MAX. 10 PETICIONES)
API_KEY_GOOGLE = os.getenv("API_KEY_GOOGLE")

# Leemos el indentificador
SEARCH_ENGINE_ID = os.getenv("SEARCH_ENGINE_ID")

query = 'Daniel Rodriguez Zavaleta'

def main_google():
    gsearch = GoogleSearch(API_KEY_GOOGLE, SEARCH_ENGINE_ID)
    results = gsearch.search(query=query)

    print(results)

def main_duck():
    dsearch = DuckSearch()
    results = dsearch.search(query=query)

    print(results)

if __name__ == '__main__':
    main_google()