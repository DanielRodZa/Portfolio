from dotenv import load_dotenv
import os

from googleSearch import GoogleSearch

# Cargamos las variables de entorno
load_dotenv()

# Leemos la clave API (MAX. 10 PETICIONES)
API_KEY_GOOGLE = os.getenv("API_KEY_GOOGLE")

# Leemos el indentificador
SEARCH_ENGINE_ID = os.getenv("SEARCH_ENGINE_ID")

query = 'Daniel Rodriguez Zavaleta'

gsearch = GoogleSearch(API_KEY_GOOGLE, SEARCH_ENGINE_ID)
results = gsearch.search(query=query)

print(results)
