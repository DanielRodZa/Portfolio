import time
import requests

from url_download import descargar_archivo
from datetime import datetime
from bs4 import BeautifulSoup

def solicitar_url(url_principal, name):
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
