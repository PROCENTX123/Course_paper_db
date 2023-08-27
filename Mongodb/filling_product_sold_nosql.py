import random

from pymongo import MongoClient

#открытие коннекта
client = MongoClient("mongodb://localhost:27017/")
mydb = client['course_paper']
col_sold = mydb["product_sold"]

class ProductSold:
    def __init__(self, id, product_id, task_id, units, price_per_unit, price, client_id):
        self.id = id
        self.product_id = product_id
        self.task_id = task_id
        self.units = units
        self.price_per_unit = price_per_unit
        self.price = price
        self.client_id = client_id

    def __dict__(self):
        return {
            "id": self.id,
            "product_id": self.product_id,
            "task_id": self.task_id,
            "units": self.units,
            "price_per_unit": self.price_per_unit,
            "price": self.price,
        }

def fill_product_sold(task_dict, arr_for_sale, product_dict):
    product_sold_dict = {}
    id = 1
    for key_task, value_task in task_dict.items():
        if value_task.id in arr_for_sale:
            id_product = random.choice(list(product_dict.keys()))
            sold = ProductSold(id, id_product, key_task, product_dict[id_product].unit,
                                product_dict[id_product].price_per_unit,
                                product_dict[id_product].unit * product_dict[id_product].price_per_unit,
                                value_task.client_id)
            col_sold.insert_one(sold.__dict__())
            product_sold_dict[id] = sold
            id += 1
    return product_sold_dict