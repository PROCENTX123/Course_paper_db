from pymongo import MongoClient
from itertools import product

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
        self._name_lastname_user = name_lastname_user

    def __dict__(self):
        return {
            "id": self.id,
            "first_name": self.first_name,
            "lastname": self.last_name,
            "user_name": self.user_name,
            "password": self.password
        }


def fill_user_account(id ,arr_name, arr_lastname, arr_username, arr_passwords):
    user_dict = {}
    for name, lastname, username, password in product(arr_name, arr_lastname, arr_username, arr_passwords):
        name_lastname = f"{name} {lastname}"
        user_account = UserAccount(id, name, lastname, username, password, name_lastname)
        col_user_account.insert_one(user_account.__dict__())
        user_dict[id] = user_account
        id+=1
    return user_dict



