from pymongo import MongoClient
from itertools import product
from tqdm import tqdm

#открытие коннекта
client = MongoClient("mongodb://localhost:27017/")
mydb = client['course_paper']
col_call = mydb["call"]

class Call:
    def __init__(self, id, user_account_id, task_id, start_time, end_time, client_id, client_name):
        self.id = id
        self.user_account_id = user_account_id
        self.task_id = task_id
        self.start_time = start_time
        self.end_time = end_time
        self.client_id = client_id
        self.client_name = client_name

    def __dict__(self):
        return {
            "call_id": self.id,
            "user_account_id": self.user_account_id,
            "task_id": self.task_id,
            "start_time": self.start_time,
            "end_time": self.end_time,
            "client_id": self.client_id,
            "client_name": self.client_name
        }
    def to_dict(self):
        return self.__dict__()

def fill_call(task_dict, arr_pair_for_call, arr_start_time, arr_end_time):
    calls_list = []
    call_doc_list = []
    id = 1
    total_items = len(task_dict) / 4
    with tqdm(total= total_items, desc="Filling call dict") as pbar:
        for user_task_client in arr_pair_for_call:
            for start_time, end_time in product(arr_start_time, arr_end_time):
                call = Call(id, user_task_client[0], user_task_client[1], start_time, end_time, user_task_client[2],
                                  user_task_client[3])

                calls_list.append((id, user_task_client[0], user_task_client[1], start_time, end_time, user_task_client[2],
                                  user_task_client[3]))
                call_doc_list.append(call.to_dict())
                id += 1
                pbar.update(1)
        # for key, value in list(task_dict.items())[index:]:
        #     if len(calls_dict) == total_items:
        #         break
        #     elif (value.user_assigned, value.id) in arr_pair_for_call:
        #         for start_time, end_time in product(arr_start_time, arr_end_time):
        #             call = Call(id, value.user_assigned, value.id, start_time, end_time, value.client_id, value.client_name)

    col_call.insert_many(call_doc_list)
    print("Call list completed")
    return calls_list