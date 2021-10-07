from AsosModel import Asos
from FarfetchModel import Farfetch
from databaseModel import Database

class MainController(object):
    def getSneakerList(self, id: int):
        params = Database.getInfo(self=Database, id=id)
        SneakerList = []
        for item in Asos.loadList(Asos,params['gender'],params['brand'],params['color'],params['priceLow'], params['priceHigh'], float(params['size'])):
            SneakerList.append(item)
        print('Asos отстрелялся')
        for item in Farfetch.loadList(Farfetch,params['gender'],params['brand'],params['color'],params['priceLow'], params['priceHigh'], float(params['size'])):
            SneakerList.append(item)
        print('farfetch отстрелялся')
        return SneakerList

