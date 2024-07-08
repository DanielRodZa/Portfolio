import csv
import requests

def leer_urls(archivo):
    urls = []
    with open(archivo, 'r', encoding='utf-8') as archivo_csv:
        lector_csv = csv.DictReader(archivo_csv)

        for fila in lector_csv:
            if fila['is_gallery'].lower() == 'true':
                # print(f'Este link es una galeria: {fila["URL"]}')
                print(fila)
            else:
                urls.append(fila['URL'])

    return urls


def descargar_archivo(url, directorio='', nombre_archivo=None, gallery=False):
    try:
        respuesta = requests.get(url)
        print(f'{respuesta.status_code} - {url}' )
        respuesta.raise_for_status()

        if not nombre_archivo:
            nombre_archivo = f'{directorio}/{url.split("/")[-1]}'
        else:
            nombre_archivo = f'{directorio}/{nombre_archivo}.jpg'

        if not gallery:
            extension = nombre_archivo.split('.')[-1].lower()
            if extension not in ['jpg', 'jpeg', 'gif', 'png', 'webp', 'mp4']:
                raise ValueError("Formato de archivo no válido")

        with open(nombre_archivo, 'wb') as archivo:
            archivo.write(respuesta.content)

    except requests.exceptions.RequestException as e:
        print(f"Error al descargar el archivo: {e}")

    except ValueError as e:
        print(f"Error: {e}")
