import csv
import time

import requests
from datetime import datetime
from bs4 import BeautifulSoup



def leer_urls(archivo):
    urls = []
    galerias = []
    with open(archivo, 'r', encoding='utf-8') as archivo_csv:
        lector_csv = csv.DictReader(archivo_csv)

        for fila in lector_csv:
            if fila['is_gallery'].lower() == 'true':
                galerias.append(fila['URL'])
            else:
                urls.append(fila['URL'])

    return urls, galerias


def descargar_archivo(url, directorio='', nombre_archivo=None, gallery=False):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9/',
            'age': '5297106'
            }
        if 'imgur' and 'gifv' in url:
            headers = {
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
                'Accept': 'video/webm,video/ogg,video/*;q=0.9,application/ogg;q=0.7,audio/*;q=0.6,*/*;q=0.5',
                'age': '5297106'
                }
            url = url.replace('gifv', 'mp4')
        respuesta = requests.get(url, headers=headers)
        time.sleep(1)
        # print(f'{respuesta.status_code} - {url}' )
        respuesta.raise_for_status()

        if not nombre_archivo:
            nombre_archivo = f'{directorio}/{url.split("/")[-1]}'
        else:
            nombre_archivo = f'{directorio}/{nombre_archivo}.jpg'

        if not gallery:
            extension = nombre_archivo.split('.')[-1].lower()
            if extension not in ['jpg', 'jpeg', 'gif', 'png', 'webp', 'gifv', 'mp4']:
                raise ValueError("Formato de archivo no válido")

        with open(nombre_archivo, 'wb') as archivo:
            archivo.write(respuesta.content)

    except requests.exceptions.RequestException as e:
        print(f"Error al descargar el archivo: {e}")

    except ValueError as e:
        print(f"Error: {e}")


def descargar_galeria(url_principal, name):
    response = requests.get(url_principal)
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    figure_elements = soup.find_all('figure')
    for figure_element in figure_elements:
        primer_link = figure_element.find('a')['href']
        descargar_archivo(
            url=primer_link,
            directorio=name,
            nombre_archivo=f'imagen_{datetime.now().strftime("%Y-%m-%d_%H-%M-%S")}',
            gallery=True
        )
