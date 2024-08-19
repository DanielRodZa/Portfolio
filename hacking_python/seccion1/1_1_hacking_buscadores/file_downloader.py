import os
import requests


class FileDownloader:
    def __init__(self, directorio_destino):
        self.directorio_destino = directorio_destino
        self.directorio_destino()

    def crear_directorio(self):
        if not os.path.exists(self.directorio_destino):
            os.mkdir(self.directorio_destino)

    def descargar_archivo(self, url):
        try:
            respuesta = requests.get(url)
            nombre_archivo = url.split('/')[-1]
            ruta_completa = os.path.join(self.directorio_destino, nombre_archivo)
            # Guardamos el archivo en disco
            with open(ruta_completa, 'wb') as archivo:
                archivo.write(respuesta.content)
            print(f"Archivo: {nombre_archivo} descargado en: {ruta_completa}.")
        except Exception as e:
            print(f"Error al descargar archivo, error: {e}")

    def filtro_descargas(self, urls, tipos_archivos=None):
        if tipos_archivos == ["all"]:
            for url in urls:
                self.descargar_archivo(url)
        else:
            for url in urls:
                if any(url.endswith(f".{tipo}") for tipo in tipos_archivos):
                    self.descargar_archivo(url)
