from pymongo import MongoClient
from itertools import product
from tqdm import tqdm
import time

#открытие коннекта
client = MongoClient("mongodb://localhost:27017/")
mydb = client['course_paper']
col_user_account = mydb["user_account"]

class UserAccount:

    def __init__(self, id, first_name, last_name, user_name, password, name_lastname_user):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.user_name = user_name
        self.password = password
        self.name_lastname_user = name_lastname_user

    def __dict__(self):
        return {
            "id": self.id,
            "first_name": self.first_name,
            "lastname": self.last_name,
            "user_name": self.user_name,
            "password": self.password,
            "name_lastname_user": self.name_lastname_user
        }
    def to_dict(self):
        return self.__dict__()


def fill_user_account(arr_name, arr_lastname, arr_username, arr_passwords):
    user_dict = {}
    user_doc_list = []
    id = 1
    total_items = len(arr_name) * len(arr_lastname) * len(arr_username) * len(arr_passwords)


    with tqdm(total=total_items, desc="Filling user account") as pbar:
        for name, lastname, username, password in product(arr_name, arr_lastname, arr_username, arr_passwords):
            name_lastname = f"{name} {lastname}"
            user_account = UserAccount(id, name, lastname, username, password, name_lastname)
            user_account_doc = user_account.to_dict()
            user_doc_list.append(user_account_doc)
            user_dict[id] = user_account
            id+=1

            pbar.update(1)
    time_start = time.time()
    col_user_account.insert_many(user_doc_list)
    time_end = time.time()
    print(f"Запись данных юзеров {time_end - time_start}")
    # print("User_account completed")
    return user_dict


# if __name__ == "__main__":
#     col_user_account = mydb["user_account"]
#     col_user_account.drop()
#
#     arr_name = ["Roman", "Ivan", "Vladimir", "Dmitriy", "Nikita"]
#     arr_lastname = ["Grigorev", "Ivanov", "Petrov", "Sidorov", "X"]
#     arr_username = ["Procent", "Lox", "MOx", "Bubaleh", "uxz"]
#     arr_passwords = ["12345", "54321", "11111", "123", "00000"]
#     id = 1
#
#     dict = fill_user_account(arr_name, arr_lastname, arr_username, arr_passwords)
#     # document = col_user_account.find()# курсор
#     #
#     # for doc in document:
#     #     print(doc['first_name'])
#     target_name = 'Sidorov'
#     pipeline = [
#         {"$match": {"lastname": target_name}},
#         {"$project": {"name_lastname_user": 1, "id": 1}}
#     ]
#     result = mydb['user_account'].aggregate(pipeline)
#     for doc in result:
#         print(doc['name_lastname_user'])


