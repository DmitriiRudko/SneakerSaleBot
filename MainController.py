from AsosModel import Asos
from FarfetchModel import Farfetch

class MainController(object):
    def getSneakerList(self, gender: int, brand: str, color: str, priceLow: int, priceHigh: int, size: str or int):
        SneakerList = []
        for item in Asos.loadList(Asos,gender,brand,color,priceLow,priceHigh,size):
            SneakerList.append(item)
        print('Asos отстрелялся')
        for item in Farfetch.loadList(Farfetch,gender,brand,color, priceLow,priceHigh, size):
            SneakerList.append(item)
        print('farfetch отстрелялся')
        return SneakerList

