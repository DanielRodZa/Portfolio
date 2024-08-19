import json
from rich.console import Console
from rich.table import Table


class ResultsParser:
    def __init__(self, resultados):
        self.resultados = resultados

    def exportar_html(self, archivo_salida):
        with open("html_template.html", "r", encoding="utf-8") as f:
            plantilla = f.read()

        elementos_html = ''
        for indice, resultado in enumerate(self.resultados, start=1):
            elemento = (f'<div class="resultados">'
                        f'<div class="indice">Resultado {indice}</div>'
                        f'<h5>{resultado["title"]}</h5>'
                        f'<p>{resultado["description"]}</p>'
                        f'<a href="{resultado["link"]}">{resultado["link"]}</a>'
                        f'</div>')
            elementos_html += elemento
        informe_html = plantilla.replace('{{ resultados }}', elementos_html)
        with open(archivo_salida, "w", encoding="utf-8") as f:
            f.write(f"{informe_html}.html")
        print(f"Resultados exportados a HTML. Fichero creado: {archivo_salida}")

    def exportar_json(self, archivo_salida):
        with open(archivo_salida, "w", encoding="utf-8") as f:
            json.dump(self.resultados, f, ensure_ascii=False, indent=4)
        print(f"Resultados exportados a JSON. Fichero creado: {archivo_salida}")

    def mostrar_pantalla(self):
        console = Console()
        table = Table(show_header=True, header_style="bold magenta")
        table.add_column("#", style="dim", width=5)
        table.add_column("Título", width=50)
        table.add_column("Descripción")
        table.add_column("Enlace")

        for indice, resultado in enumerate(self.resultados, start=1):
            table.add_row(
                str(indice),
                resultado["title"],
                resultado["description"],
                resultado["link"]
                )

        console.print(table)