import random
from pymongo import MongoClient
from tqdm import tqdm

#открытие коннекта
client = MongoClient("mongodb://localhost:27017/")
mydb = client['course_paper']
col_sold = mydb["product_sold"]

class ProductSold:
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
            "sold_id": self.id,
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

def fill_product_sold(task_dict, arr_for_sale, product_list):
    product_sold_list = []
    sold_doc_list = []
    id = 1
    total_sold = len(task_dict) / 4
    with tqdm(total=total_sold, desc="Filling sold") as pbar:
        for from_task in arr_for_sale:
            product = random.choice(product_list)
            sold = ProductSold(id, product[0], from_task[0], product[2], product[3], product[2] * product[3],
                               from_task[1], from_task[2], from_task[3], from_task[4])
            sold_doc_list.append(sold.to_dict())
            product_sold_list.append((id, product[0], from_task[0], product[2], product[3], product[2] * product[3],
                               from_task[1], from_task[2], from_task[3], from_task[4]))
            id += 1
            pbar.update(1)

        # for key_task, value_task in list(task_dict.items())[index:]:
        #     if len(product_sold_dict) == total_sold:
        #         break
        #     elif value_task.id in arr_for_sale:
        #         id_product = random.choice(list(product_dict.keys()))
        #         sold = ProductSold(id, id_product, key_task, product_dict[id_product].unit,
        #                             product_dict[id_product].price_per_unit,
        #                             product_dict[id_product].unit * product_dict[id_product].price_per_unit,
        #                             value_task.client_id, value_task.client_name,
        #                             value_task.start_time, value_task.end_time)


    col_sold.insert_many(sold_doc_list)
    print("Sold completed")
    return product_sold_list