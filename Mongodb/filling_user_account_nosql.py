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

arr_name = ["Roman", "Ivan", "Vladimir", "Dmitriy", "Nikita"]
arr_lastname = ["Grigorev", "Ivanov", "Petrov", "Sidorov", "X"]
arr_username = ["Procent", "Lox", "MOx", "Bubaleh", "uxz"]
arr_passwords = ["12345", "54321", "11111", "123", "00000"]
id = 1




def fill_user_account(id ,arr_name, arr_lastname, arr_username, arr_passwords):
    #удаление старой старой коллекции
    # col_user_account.drop()

    for name, lastname, username, password in product(arr_name, arr_lastname, arr_username, arr_passwords):
        user_account = UserAccount(id, name, lastname, username, password)
        user_account_dict = vars(user_account)
        x = col_user_account.insert_one(user_account_dict)
        id+=1

#fixme когда создастся общий __main__ убрать
fill_user_account(id ,arr_name, arr_lastname, arr_username, arr_passwords)

#Закрытие конекта
client.close()
