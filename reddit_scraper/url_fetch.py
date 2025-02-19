import os
import time
import httpx
import pandas as pd

from request_gallery import solicitar_url


def url_fetch(name):
    base_url = 'https://www.reddit.com'
    endpoint = f'{name}'
    category = ''
    url = base_url + endpoint + category + '.json'
    after_post_id = None

    dataset = []
    data = []

    while True:
        params = {
            'limit': 100,
            't': 'year',
            'after': after_post_id
        }
        response = httpx.get(url, params=params)
        print(f'fetching "{response.url}"...=')
        if response.status_code != 200:
            print(f'Failed to fetch data: {response.status_code}')

        json_data = response.json()

        dataset.extend([rec['data'] for rec in json_data['data']['children']])

        after_post_id = json_data['data']['after']
        time.sleep(0.5)

        for x in json_data['data']['children']:
            dividir_links(x, data)

        if after_post_id == None:
            break

    nombre_csv_links = create_dataframes(dataset, data, name)

    return nombre_csv_links


def create_dataframes(dataset, data, name):
    dir_name = name.split('/')[-1]
    df = pd.DataFrame(dataset)
    df.to_csv(f'{dir_name}/{dir_name}.csv', index=False)

    nombre_csv_links = f'{dir_name}/{dir_name}_links.csv'
    df = pd.DataFrame(data)
    df = df.drop_duplicates(subset=['URL'])
    df.to_csv(nombre_csv_links, index=False)

    return nombre_csv_links


def dividir_links(x, data):
    try:
        post_url = x['data']['url']
        post_name = x['data']['title']
        user = x['data']['subreddit']
        if 'is_gallery' in x['data']:
            is_gallery = True
            gallery_data = x['data']['gallery_data']
        else:
            is_gallery = False
            gallery_data = ''
        data.append({'Subreddit': user, 'Título': post_name, 'is_gallery': is_gallery, 'URL': post_url, 'gallery_data': gallery_data})
    except KeyError as ke:
        print(f'El post no tiene un elemento: {ke}')
    except Exception as e:
        print(f'Hubo un error: {e}')
