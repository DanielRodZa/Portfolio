import requests


class GoogleSearch:
    def __init__(self, api_key, engine_id) -> None:
        """
        Inicializa una nueva instancia de GoogleSearch.

        Permite realizar peticiones automatizadas a la API de Google

        Args:
            api_key (str): Clave API de Google
            engine_id (str): Identificador del motod de busqueda personalizado de Google.

        """
        self.api_key = api_key
        self.engine_id = engine_id

    def search(self, query, start_page=1, pages=1, lang="lang_es"):
        """
        Realiza una busqueda en Google utilizando su API

        Args:
            query (str): String de la busqueda a realizar
            start_page (int): Número de página incial, default -> 1
            pages (int): Número de páginas a visitar, default -> 1
            lang (str): Lenguaje de la busqueda, default -> lang_es
        """
        final_results = []
        results_per_page = 10  # Google muestra por defecto 10 resultados por pagina
        for page in range(pages):
            # Calcular el resultado de comienzo de cada pagina
            start_index = (start_page - 1) * results_per_page + 1 + (page * results_per_page)
            url = f"https://www.googleapis.com/customsearch/v1?key={self.api_key}&cx={self.engine_id}&q={query}&start={start_index}&lr={lang}"
            response = requests.get(url)
            # Comprobamos si la respuesta el correcta
            if response.status_code == 200:
                data = response.json()
                results = data.get("items")
                cresults = self.custom_results(results)
                final_results.extend(cresults)
            else:
                print(f"Error obtenido al consultar la página: {response.status_code}")
                break
        return final_results

    def custom_results(self, results):
        """
        Filtra los resultados de la consulta.
        Returns:
            custom_results (list): Lista de resultados de la busqueda.
        """
        custom_results = []
        for r in results:
            cresult = {}
            cresult["title"] = r.get("title")
            cresult["description"] = r.get("snippet")
            cresult["link"] = r.get("link")
            custom_results.append(cresult)
        return custom_results
