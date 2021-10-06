import requests
import SneakerClass
from FarfetchArrayParams import brands
from FarfetchArrayParams import colors
from FarfetchArrayParams import sizes


class Farfetch(object):
    def __init__(self):
        self.session = requests.Session()
        self.session.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36',
            'Accept-Language': 'ru',
        }

    def loadList(self, gender: int, brand: str, color: str, priceLow: int, priceHigh: int, size: str or int):
        if (gender):
            gender = 'Men'
        else:
            gender = 'Women'
        url = 'https://www.farfetch.com/ru/plpslice/listing-api/products-facets?'
        requestParams = {'view': 250 , 'scale': 282 , 'rootCategory': gender , 'pagetype': 'Shopping', 'pricetype': 'fullprice', 'c-category': 137174,
                         'c-designer': brands[brand], 'size': sizes[size], 'colour' : colors[color], 'price' : str(priceLow)+'-'+str(priceHigh)}
        req = requests.get(url=url, params=requestParams)
        responese = req.json()
        sneakerList = responese['listingItems']['items']
        return self.jsonPars(self,sneakerList)

    def jsonPars(self, jsonList: dict):
        productList = []
        for product in jsonList:
            productList.append(SneakerClass.Sneaker(product['brand']['name'] + ' ' + product['shortDescription'], product['priceInfo']['formattedFinalPrice'], 'https://www.farfetch.com/' + product['url'], product['images']['model']))
        return productList
