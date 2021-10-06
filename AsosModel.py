import requests

import AsosArrayParams
import SneakerClass
from AsosArrayParams import brands
from AsosArrayParams import sizes
from AsosArrayParams import colors


class Asos(object):
    def loadList(self, gender: int, brand: str, color: str, priceLow: int, priceHigh: int, size: int):
        if (brand == 'adidas'):
            sizes = AsosArrayParams.adidasSizes
        else:
            sizes = AsosArrayParams.sizes
        requestParams = {'brand': brands[brand], 'base_color': colors[color], 'channel': 'desktop-web', 'country': 'RU',
                         'currency': 'RUB', 'discount_band': 2,
                         'keyStoreDataversion': 'hgk0y12-29', 'lang': 'ru-RU', 'limit': 100, 'offset': -100,
                         'priceMax': priceHigh, 'priceMin': priceLow, 'rowlength': 4, 'size': sizes[size], 'store': 'RU'}
        if (gender):
            url = 'https://www.asos.com/api/product/search/v2/categories/4209?'
        else:
            url = 'https://www.asos.com/api/product/search/v2/categories/4172?'
        req = requests.get(url=url, params=requestParams)
        responese = req.json()
        return self.jsonPars(self, responese, brand)

    def jsonPars(self, jsonlist: dict, brand: str):
        productList = []
        for product in jsonlist['products']:
            name = product['name']
            productList.append(SneakerClass.Sneaker(name[name.find(brand):], product['price']['current']['text'], ('https://www.asos.com/ru/' + product['url']), 'https://' + product['imageUrl']))
        return productList




