from pymongo import MongoClient
from itertools import product

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

def get_client_name():
    collection = mydb["client"]
    return [f"{i['client_name']}" for i in collection.find()]

def get_name_lastname_user():
    collection = mydb["user_account"]
    return [f"{i['first_name']} {i['last_name'] }" for i in collection.find()]

def fill_task(client_name,  user_first_last_name, arr_client_and_user, arr_start_time, arr_end_time):
    id = 1

    arr_pairs_for_meeting = []
    arr_pairs_for_calls = []
    arr_for_sale = []
    arr_for_offered = []



    count_all_task = len(arr_client_and_user) * len(arr_start_time) * len(arr_end_time)
    #fixme поправить это место, если что set[0,0] это id клиента set[0][1] прикрепленный к нему юзер set[1] имя клиента set[2] фамилия имя юзера
    for set in zip(arr_client_and_user, client_name, user_first_last_name):
        for start_time, end_time in product(arr_start_time, arr_end_time):
            task = Task(id, set[0][0], set[1], start_time, end_time, set[0][1], set[2])
            if id > count_all_task * 0.25 and id <= count_all_task * 0.5:
                arr_pairs_for_calls.append((set[0][1], id))
            elif id > 0 and id <= count_all_task * 0.25:
                arr_pairs_for_meeting.append((set[0][1], id))
            elif id > count_all_task * 0.5 and id <= count_all_task * 0.75:
                arr_for_sale.append(id)
            elif id > count_all_task * 0.75 and id <=count_all_task:
                arr_for_offered.append(id)
            task_dict = vars(task)
            col_task.insert_one(task_dict)
            id += 1


    return arr_pairs_for_meeting, arr_pairs_for_calls, arr_for_sale, arr_for_offered