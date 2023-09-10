from pymongo import MongoClient
from itertools import product
from tqdm import tqdm
import gc
import time
import sys

#открытие коннекта
client = MongoClient("mongodb://localhost:27017/")
mydb = client['course_paper']
col_meet = mydb["meeting"]

class Meeting:
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
            "meeting_id": self.id,
            "user_account_id": self.user_account_id,
            "task_id": self.task_id,
            "start_time": self.start_time,
            "end_time": self.end_time,
            "client_id": self.client_id,
            "client_name": self.client_name
        }
    def to_dict(self):
        return self.__dict__()

def fill_meeting(arr_pair_for_meeting, arr_start_time, arr_end_time):
    meeting_list = []
    meeting_doc_list = []
    id = 1

    total_items = len(arr_pair_for_meeting)

    with tqdm(total=total_items, desc="Filling meeting") as pbar:
        for user_task_client in arr_pair_for_meeting:
            # target_value = user_task_client[1]
            # filter_query = {"id": target_value}
            # projection = {"client_name": 1}
            # result = mydb['task'].find(filter_query, projection).next()
            for start_time, end_time in product(arr_start_time, arr_end_time):
                meeting = Meeting(id, user_task_client[0], user_task_client[1], start_time, end_time, user_task_client[2],
                                  user_task_client[3])
                meeting_list.append((id, user_task_client[0], user_task_client[1], start_time, end_time, user_task_client[2],
                                  user_task_client[3]))
                meeting_doc_list.append(meeting.to_dict())

                # print(key)
                id += 1
                pbar.update(1)

        # for key, value in task_dict.items():
        #     if len(meeting_dict) == total_items:
        #         break
        #     elif (value.user_assigned, value.id) in arr_pair_for_meeting:
        #         for start_time, end_time in product(arr_start_time, arr_end_time):
        #             meeting = Meeting(id, value.user_assigned, value.id, start_time, end_time, value.client_id,
        #                               value.client_name)

    size_in_bytes = sys.getsizeof(meeting_doc_list)
    print(f"Размер списка в байтах: {size_in_bytes} байт")

    time_start = time.time()
    col_meet.insert_many(meeting_doc_list)
    time_end = time.time()
    # print(f"Запись данных встреч {time_end - time_start}")

    # print("Meeting completed")

    del meeting_doc_list
    del arr_pair_for_meeting
    gc.collect()
    return meeting_list