from pymongo import MongoClient
from itertools import product
from tqdm import tqdm

#открытие коннекта
client = MongoClient("mongodb://localhost:27017/")
mydb = client['course_paper']
col_task = mydb["task"]

class Task:
    def __init__(self, id, client_id, client_name, start_time, end_time, user_assigned, user_first_last_name):
        self.id = id
        self.client_id = client_id
        self.client_name = client_name
        self.start_time = start_time
        self.end_time = end_time
        self.user_assigned = user_assigned
        self.user_first_last_name = user_first_last_name

    def __dict__(self):
        return {
            "id": self.id,
            "client_id": self.client_id,
            "client_name": self.client_name,
            "start_time": self.start_time,
            "end_time": self.end_time,
            "user_assigned": self.user_assigned,
            "user_name_lastname": self.user_first_last_name
        }
    def to_dict(self):
        return self.__dict__()


def fill_task(client_dict, arr_start_time, arr_end_time):
    id = 1
    task_dict = {}
    task_doc_list = []

    arr_pairs_for_meeting = []
    arr_pairs_for_calls = []
    arr_for_sale = []
    arr_for_offered = []



    count_all_task = len(client_dict) * len(arr_start_time) * len(arr_end_time) # количество задач

    with tqdm(total=count_all_task, desc="Filling task") as pbar:
        for key, value in client_dict.items():
            for start_time, end_time in product(arr_start_time, arr_end_time):
                task = Task(id, value.id, value.client_name, start_time, end_time, value.user_inserted, value._name_lastname_user_inserted)
                if id > 0 and id <= count_all_task * 0.25:
                    arr_pairs_for_meeting.append((value.user_inserted, id, value.id, value.client_name))
                elif id > count_all_task * 0.25 and id <= count_all_task * 0.5:
                    arr_pairs_for_calls.append((value.user_inserted, id, value.id, value.client_name))
                elif id > count_all_task * 0.5 and id <= count_all_task * 0.75:
                    arr_for_sale.append((id, value.id, value.client_name, start_time, end_time))
                elif id > count_all_task * 0.75 and id <=count_all_task:
                    arr_for_offered.append((id, value.id, value.client_name, start_time, end_time))
                #fixme прочитать в клиенте
                task_doc = task.to_dict()
                task_doc_list.append(task_doc)
                task_dict[id] = task
                id += 1

                pbar.update(1)

    col_task.insert_many(task_doc_list)
    print("Task completed")
    return task_dict, arr_pairs_for_meeting, arr_pairs_for_calls, arr_for_sale, arr_for_offered