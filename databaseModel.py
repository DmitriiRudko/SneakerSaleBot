import pymysql
from configDB import *

class Database(object):
    def connectDb(self):
        connection = pymysql.connect(
            host=host,
            port=3306,
            user=user,
            password=password,
            database=db_name,
            cursorclass=pymysql.cursors.DictCursor
        )
        return connection
    def addUser(self,id: int):
        connection = self.connectDb(self)
        try:
            with connection.cursor() as cursor:
                addUserQuery = f"INSERT INTO `users` (id, color, size, brand, gender, priceLow, priceHigh) VALUES ({id}, 'any', '40', 'Nike', 1, 0, 10000)"
                cursor.execute(addUserQuery)
                connection.commit()
        except:
            print('Дубликат')
        finally:
            connection.close()
    def changeParams(self,id: int, param: str, value):
        connection = self.connectDb(self)
        try:
            with connection.cursor() as cursor:
                if (param=='color' or param=='size' or param=='brand'):
                    changeParamQuery = f"UPDATE `users` SET {param}='{value}' WHERE id={id}"
                else:
                    changeParamQuery = f"UPDATE `users` SET {param}={value} WHERE id={id}"
                cursor.execute(changeParamQuery)
                connection.commit()
        finally:
            connection.close()
    def getInfo(self,id: int):
        connection = self.connectDb(self)
        try:
            with connection.cursor() as cursor:
                getInfoQuery = f"SELECT * FROM `users` WHERE id={id}"
                cursor.execute(getInfoQuery)
                info = cursor.fetchone()
        finally:
            return info




