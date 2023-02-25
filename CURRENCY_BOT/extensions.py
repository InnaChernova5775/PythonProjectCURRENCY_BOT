import requests
import json
from CURRENCY_BOT.config import keys

class APIException (Exception):
    pass
class CarrencyConverter:
    @staticmethod
    def get_price(quote:str,base:str,amount:str):
        if quote==base:
            raise APIException (f'Невозможно обработать одинаковые валюты {base}.')
        try:
            quote_ticket=keys[quote]
        except KeyError:
            raise APIException (f'Введено неправильное название валюты {quote}.')
        try:
            base_ticket=keys[base]
        except KeyError:
            raise APIException (f'Введено неправильное название валюты: {base}.')
        try:
            amount=float(amount)
        except ValueError:
            raise APIException (f'Не удалось обработать количество {amount}.')

        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={quote_ticket}&tsyms={base_ticket}')
        total_base =json.loads(r.content)[keys[base]]
        return total_base