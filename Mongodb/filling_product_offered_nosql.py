import random
from pymongo import MongoClient
from tqdm import tqdm
import gc
import time

#открытие коннекта
client = MongoClient("mongodb://localhost:27017/")
mydb = client['course_paper']
col_offer = mydb["product_offered"]

class ProductOffered:
    def __init__(self, id, product_id, task_id, units, price_per_unit, price, client_id, client_name, start_time, end_time):
        self.id = id
        self.product_id = product_id
        self.task_id = task_id
        self.units = units
        self.price_per_unit = price_per_unit
        self.price = price
        self.client_id = client_id
        self.client_name = client_name
        self.start_time = start_time
        self.end_time = end_time

    def __dict__(self):
        return {
            "offer_id": self.id,
            "product_id": self.product_id,
            "task_id": self.task_id,
            "units": self.units,
            "price_per_unit": self.price_per_unit,
            "price": self.price,
            "client_id": self.client_id,
            "client_name": self.client_name,
            "start_time": self.start_time,
            "end_time": self.end_time
        }
    def to_dict(self):
        return self.__dict__()

def fill_product_offered(arr_for_offer, product_list):
    product_offer_list = []
    offer_doc_list = []
    id = 1
    total = len(arr_for_offer)
    with tqdm(total=total, desc="Filling offer") as pbar:
        for from_task in arr_for_offer:
            product = random.choice(product_list)
            offer = ProductOffered(id, product[0], from_task[0], product[2], product[3], product[2] * product[3],
                               from_task[1], from_task[2], from_task[3], from_task[4])
            offer_doc_list.append(offer.to_dict())
            product_offer_list.append((id, product[0], from_task[0], product[2], product[3], product[2] * product[3],
                                       from_task[1], from_task[2], from_task[3], from_task[4]))
            id += 1
            pbar.update(1)
        # for key_task, value_task in list(task_dict.items())[index:]:
        #     if len(product_offer_dict) == total:
        #         break
        #     elif value_task.id in arr_for_offer:
        #         id_product = random.choice(list(product_dict.keys()))
        #         offer = ProductOffered(id, id_product, key_task, product_dict[id_product].unit,
        #                             product_dict[id_product].price_per_unit,
        #                             product_dict[id_product].unit * product_dict[id_product].price_per_unit,
        #                             value_task.client_id, value_task.client_name,
        #                                value_task.start_time, value_task.end_time)

    time_start = time.time()
    col_offer.insert_many(offer_doc_list)
    time_end = time.time()
    print(f"Запись данных рекомендаций {time_end - time_start}")
    # print("Offer completed")

    del offer_doc_list
    del arr_for_offer
    gc.collect()

    return product_offer_list