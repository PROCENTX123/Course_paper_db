import random

from pymongo import MongoClient

#открытие коннекта
client = MongoClient("mongodb://localhost:27017/")
mydb = client['course_paper']
col_offer = mydb["product_offered"]

class ProductOffered:
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
            "client_id": self.client_id
        }

def fill_product_offered(task_dict, arr_for_offer, product_dict):
    product_offer_dict = {}
    id = 1
    for key_task, value_task in task_dict.items():
        if value_task.id in arr_for_offer:
            id_product = random.choice(list(product_dict.keys()))
            offer = ProductOffered(id, id_product, key_task, product_dict[id_product].unit,
                                product_dict[id_product].price_per_unit,
                                product_dict[id_product].unit * product_dict[id_product].price_per_unit,
                                value_task.client_id)
            col_offer.insert_one(offer.__dict__())
            # product_offer_dict[value_task.client_id] = key_task, id, id_product, product_dict[id_product].unit, product_dict[id_product].unit * product_dict[id_product].price_per_unit
            product_offer_dict[id] = offer
            id += 1
    return product_offer_dict