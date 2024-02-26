import os
import argparse

from urllib.parse import urlparse
from dotenv import load_dotenv

import requests

load_dotenv()


def is_bitlink(url, bitly_api_token):
    is_bitlink_url = f'https://api-ssl.bitly.com/v4/bitlinks/{url}'
    headers = {
        'Authorization': f'Bearer {bitly_api_token}',
    }
    response = requests.get(is_bitlink_url, headers=headers)
    return response.ok


def shorten_url(url, bitly_api_token):
    BITLY_URL = 'https://api-ssl.bitly.com/v4/bitlinks'
    headers = {
        'Authorization': f'Bearer {bitly_api_token}',
    }
    payload = {
        'long_url': url
    }
    response = requests.post(BITLY_URL, json=payload, headers=headers)
    response.raise_for_status()
    return response.json()['link']


def get_bitlink(bitlink):
    parsed_url = urlparse(bitlink)
    return f'{parsed_url.netloc}{parsed_url.path}'


def count_clicks(bitlink_id, bitly_api_token):
    clicks_url = f'https://api-ssl.bitly.com/v4/bitlinks/{bitlink_id}/clicks/summary'
    headers = {
        'Authorization': f'Bearer {bitly_api_token}',
    }
    response = requests.get(clicks_url, headers=headers)
    response.raise_for_status()
    return response.json()['total_clicks']


def createParser():
    parser = argparse.ArgumentParser(
        description='Программа сокращает ссылку и считает количество кликов по уже сокращенной ссылке'
    )
    parser.add_argument('-url', help='Ссылки')
    return parser


def main():
    parser = createParser()
    args = parser.parse_args()
    bitly_api_token = os.environ.get('BITLY_API_TOKEN')
    if args.url is not None:
        url = args.url
    else:
        url = input('Введите ссылку: ')
    bitlink_id = get_bitlink(url)
    try:
        if is_bitlink(bitlink_id, bitly_api_token):
            print(f'Количество кликов по ссылке {bitlink_id}: {count_clicks(bitlink_id, bitly_api_token)}')
        else:
            print(f'Битлинк: {shorten_url(url, bitly_api_token)}')
    except requests.exceptions.HTTPError as error:
        print(f'Ошибка: {error}')
    except requests.exceptions.ConnectionError as e:
        print(f'Ошибка: {e}')


if __name__ == '__main__':
    main()
