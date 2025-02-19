from tqdm import tqdm
import errno
import argparse
import os

from url_fetch import url_fetch
from url_download import leer_urls, descargar_archivo, descargar_galeria


def main(name):

    try:
        dir_name = name.split('/')[-1]
        os.mkdir(dir_name)
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise


    nombre_archivo = url_fetch(name)
    lista_urls, lista_galerias = leer_urls(nombre_archivo)

    for url in tqdm(lista_urls, "Descargando archivos"):
        descargar_archivo(url=url, directorio=dir_name)

    # for url in tqdm(lista_galerias, 'Descargando galerías'):
    #     descargar_galeria(url_principal=url, name=dir_name)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description="Esta herramienta permite descargar información de reddit"
    )
    parser.add_argument('-u', '--user', type=str,
                        help='usuario a buscar en reddit')
    parser.add_argument('-r', '--reddit', type=str,
                        help='reddit para buscar')
    args = parser.parse_args()
    if args.user:
        main(name=f"/user/{args.user}")
    elif args.reddit:
        main(name=f"/r/{args.reddit}")
    else:
        print('Por favor introduce un usuario o tópico')

