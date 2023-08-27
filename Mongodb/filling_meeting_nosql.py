from pymongo import MongoClient
from itertools import product

#открытие коннекта
client = MongoClient("mongodb://localhost:27017/")
mydb = client['course_paper']
col_meet = mydb["meeting"]

class Meeting:
    def __init__(self, id, user_account_id, task_id, start_time, end_time, client_id):
        self.id = id
        self.user_account_id = user_account_id
        self.task_id = task_id
        self.start_time = start_time
        self.end_time = end_time
        self.client_id = client_id

    def __dict__(self):
        return {
            "id": self.id,
            "user_account_id": self.user_account_id,
            "task_id": self.task_id,
            "start_time": self.start_time,
            "end_time": self.end_time
        }

def fill_meeting(task_dict ,arr_pair_for_meeting, arr_start_time, arr_end_time):
    meeting_dict = {}
    id = 1

    for key, value in task_dict.items():
        if (value.user_assigned, value.id) in arr_pair_for_meeting:
            for start_time, end_time in product(arr_start_time, arr_end_time):
                call = Meeting(id, value.user_assigned, value.id, start_time, end_time, value.client_id)
                col_meet.insert_one(call.__dict__())
                meeting_dict[id] = call
                id += 1
    return meeting_dict