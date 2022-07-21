import requests


def get_coin_list():
    response = requests.get('https://api.coingecko.com/api/v3/coins/markets?vs_currency=USD&order=market_cap_desc&per_page=100&page=1&sparkline=false')
    return [i['name'] for i in response.json()]


def get_coin_names():
    return list(zip(get_coin_list(), get_coin_list()))
