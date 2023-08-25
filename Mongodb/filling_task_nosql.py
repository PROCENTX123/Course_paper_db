from pymongo import MongoClient
from itertools import product

#открытие коннекта
client = MongoClient("mongodb://localhost:27017/")
mydb = client['course_paper']
col_client = mydb["task"]

class Task:
    def __init__(self, id, client_id, client_name, start_time, end_time, user_assigned, user_first_last_name):
        self.id = id
        self.client_id = client_id
        self.client_name = client_name
        self.start_time = start_time
        self.end_time = end_time
        self.user_assigned = user_assigned
        self.user_first_last_name = user_first_last_name



def fill_fill_task(id, client_id, client_name, start_time, end_time, user_assigned, user_first_last_name, arr_client_and_user, arr_start_time, arr_end_time):

    arr_pairs_for_meeting = []
    arr_pairs_for_calls = []
    arr_for_sale = []
    arr_for_offered = []
    id = 1

    count_all_task = len(arr_client_and_user) * len(arr_start_time) * len(arr_end_time)

    # for client_and_user in arr_client_and_user:
    #     for

    for client_name, client_adress, phone, email, contact_person, user_inserted in product(arr_client_name
            , arr_client_adress, arr_phone, arr_email, arr_contact_person, arr_user_inserted):

        client_account = Client(id, client_name, client_adress, phone, email, contact_person, user_inserted)
        client_account_dict = vars(client_account)
        x = col_client.insert_one(client_account_dict)
        arr_pairs.append((id, user_inserted))
        id+=1
    return arr_pairs