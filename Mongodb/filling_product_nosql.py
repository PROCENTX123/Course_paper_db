from pymongo import MongoClient
from itertools import product
from tqdm import tqdm
import gc
import time

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
    def to_dict(self):
        return self.__dict__()


def fill_product(arr_product_name, arr_unit, arr_price_per_unit, arr_units_in_stock):
    product_list = []
    product_doc_list = []
    id = 1
    total_product = len(arr_product_name) * len(arr_unit) * len(arr_price_per_unit) * len(arr_units_in_stock)
    with tqdm(total=total_product, desc="Filling product") as pbar:
        for product_name, unit, price_per_unit, units_in_stock in product(arr_product_name, arr_unit, arr_price_per_unit, arr_units_in_stock):

            product_list.append((id, product_name, unit, price_per_unit, units_in_stock))
            products = Products(id, product_name, unit, price_per_unit, units_in_stock)

            product_doc_list.append(products.to_dict())
            id+=1
            pbar.update(1)

    time_start = time.time()
    col_product.insert_many(product_doc_list)
    time_end = time.time()
    print(f"Запись данных продуктов {time_end - time_start}")
    # print("Product completed")

    del product_doc_list
    gc.collect()

    return product_list