from pymongo import MongoClient
from itertools import product

#открытие коннекта
client = MongoClient("mongodb://localhost:27017/")
mydb = client['course_paper']
col_product = mydb["product"]

class Products:

    def __init__(self, id, product_name, unit, price_per_unit, units_in_stock):
        self.id = id
        self.product_name = product_name
        self.unit = unit
        self.price_per_unit = price_per_unit
        self.units_in_stock = units_in_stock

    def __dict__(self):
        return {
            "id": self.id,
            "product_name": self.product_name,
            "unit": self.unit,
            "price_per_unit": self.price_per_unit,
            "units_in_stock": self.units_in_stock
        }


def fill_product(arr_product_name, arr_unit, arr_price_per_unit, arr_units_in_stock):
    product_dict = {}
    id = 1
    for product_name, unit, price_per_unit, units_in_stock in product(arr_product_name, arr_unit, arr_price_per_unit, arr_units_in_stock):
        products = Products(id, product_name, unit, price_per_unit, units_in_stock)
        col_product.insert_one(products.__dict__())
        product_dict[id] = products
        id+=1
    return product_dict