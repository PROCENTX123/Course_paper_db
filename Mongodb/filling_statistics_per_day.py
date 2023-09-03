from pymongo import MongoClient, ASCENDING, DESCENDING
from tqdm import tqdm
import time


#открытие коннекта
client = MongoClient("mongodb://localhost:27017/")
mydb = client['course_paper']
col_statistic = mydb["statistic"]

class Statistic:
    def __init__(self, client_name, tasks, start_time, end_time, meetings, calls,  sales, offer, price_for_sale,
                 price_for_offer, units, product_id):
        self.client_name = client_name
        self.tasks = tasks
        self.start_time = start_time
        self.end_time = end_time
        self.meetings = meetings
        self.calls = calls
        self.sales = sales
        self.offer = offer
        self.price_for_sale = price_for_sale
        self.price_for_offer = price_for_offer
        self.units = units
        self.product_id = product_id

    def __dict__(self):
        return {
            "client_name": self.client_name,
            "task_id": self.tasks,
            "start_time": self.start_time,
            "end_time": self.end_time,
            "meeting_id": self.meetings,
            "call_id": self.calls,
            "sales_id": self.sales,
            "offer_id": self.offer,
            "price_sale": self.price_for_sale,
            "price_offer": self.price_for_offer,
            "units": self.units,
            "product_id": self.product_id
        }
    def to_dict(self):
        return self.__dict__()

def filling_statistic(meeting_list, call_list, product_sold_list, product_offered_list):
    statistic_doc_list = []

    total = len(meeting_list) + len(call_list) + len(product_sold_list) + len(product_offered_list)

    id = 1

    with tqdm(total=total, desc="Filling statistic") as pbar:
        for meet in meeting_list:
            statistic = Statistic(meet[6], meet[2], meet[3], meet[4], meet[0], None, None,
                                  None, None, None, None, None)
            statistic_doc_list.append(statistic.to_dict())
            pbar.update(1)
        for call in call_list:
            statistic = Statistic(call[6], call[2], call[3], call[4],
                                  None, call[0], None, None, None, None, None, None)
            statistic_doc_list.append(statistic.to_dict())
            pbar.update(1)
        for sale in product_sold_list:
            statistic = Statistic(sale[7], sale[2], sale[8],
                                  sale[9], None, None, sale[0], None,
                                  sale[5], None, sale[3], sale[1])
            statistic_doc_list.append(statistic.to_dict())
            pbar.update(1)
        for offer in product_offered_list:
            statistic = Statistic(offer[7], offer[2], offer[8],
                                  offer[9], None, None, None, offer[0],
                                  None, offer[5], offer[3], offer[1])
            statistic_doc_list.append(statistic.to_dict())
            pbar.update(1)
    time_start = time.time()
    col_statistic.insert_many(statistic_doc_list)
    time_end = time.time()
    print(f"Запись данных статистики {time_end - time_start}")

    # col_statistic.create_index([("price_sale", ASCENDING), ("client_name", DESCENDING)])
    # col_statistic.create_index(["product_id", ASCENDING])
    # print("Statistic completed")


        # pipeline = [
        #     {"$project": {"_id": 0}},
        #     {"$unionWith": "$meeting"},
        #     {"$unionWith": "$call"},  # Объединение с collection2
        #     {"$unionWith": "$product_sold"},  # Объединение с collection3
        #     # Добавьте нужные операторы $unionWith для остальных коллекций
        #     {"$out": "statistic"}
        # ]
        # mydb['statistic'].aggregate(pipeline)
        # for doc in mydb['statistic'].find():
        #     print(doc)
        # for doc in result['cursor']['firstBatch']:
        #     print(doc)


        # for key_task, value_task in task_dict.items():
        #     for key_meeting, value_meeting in meeting_dict.items():
        #         if value_meeting.client_id == value_task.client_id and key_task == value_meeting.task_id:
        #             statistic = Statistic(value_task.client_name, key_task, value_meeting.start_time, value_meeting.end_time,
        #                                   key_meeting, None, None, None, None, None, None)
        #             col_statistic.insert_one(statistic.__dict__())
        #
        #     for key_call, value_call in call_dict.items():
        #         if value_call.client_id == value_task.client_id and key_task == value_call.task_id:
        #             statistic = Statistic(value_task.client_name, key_task, value_call.start_time, value_call.end_time,
        #                                   None, key_call, None, None, None, None, None)
        #             col_statistic.insert_one(statistic.__dict__())
        #
        #     for key_sold, value_sold in product_sold_dict.items():
        #         if value_sold.client_id == value_task.client_id and key_task == value_sold.task_id:
        #             statistic = Statistic(value_task.client_name, key_task, value_task.start_time, value_task.end_time,
        #                                   None, None, value_sold.id, None, value_sold.price, None, value_sold.units)
        #             col_statistic.insert_one(statistic.__dict__())
        #
        #     for key_offer, value_offer in product_offered_dict.items():
        #         if value_offer.client_id == value_task.client_id and key_task == value_offer.task_id:
        #             statistic = Statistic(value_task.client_name, key_task, value_task.start_time, value_task.end_time,
        #                                   None, None, None, value_offer.id, None, value_offer.price, value_offer.units)
        #             col_statistic.insert_one(statistic.__dict__())


