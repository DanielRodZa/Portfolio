from tqdm import tqdm
import errno
import os

from url_fetch import url_fetch
from url_download import leer_urls, descargar_archivo


def main():
    name = ''

    try:
        os.mkdir(name)
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise


    nombre_archivo = url_fetch(name)
    lista_urls = leer_urls(nombre_archivo)

    for url in tqdm(lista_urls, "Descargando archivos"):
        descargar_archivo(url=url, directorio=name)


if __name__ == '__main__':
    main()

