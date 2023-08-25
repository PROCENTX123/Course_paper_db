from pymongo import MongoClient
from itertools import product

#открытие коннекта
client = MongoClient("mongodb://localhost:27017/")
mydb = client['course_paper']
col_user_account = mydb["user_account"]

class UserAccount:
    def __init__(self, id, first_name, last_name, user_name, password):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.user_name = user_name
        self.password = password


def fill_user_account(id ,arr_name, arr_lastname, arr_username, arr_passwords):
    for name, lastname, username, password in product(arr_name, arr_lastname, arr_username, arr_passwords):
        user_account = UserAccount(id, name, lastname, username, password)
        user_account_dict = vars(user_account)
        x = col_user_account.insert_one(user_account_dict)
        id+=1




