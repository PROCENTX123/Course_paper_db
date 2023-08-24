from pymongo import MongoClient
from itertools import product

#data
#fixme нагенерировать данные
arr_client_name = []
arr_client_adress = []
arr_phone = []
arr_email = []
arr_contact_person = []
arr_user_inserted = []
id = 1

#открытие коннекта
client = MongoClient("mongodb://localhost:27017/")
mydb = client['course_paper']
col_client = mydb["client"]

class Client:
    def __init__(self, id, client_name, client_adress, phone, email, contact_person, user_inserted):
        self.id = id
        self.client_name = client_name
        self.client_adress = client_adress
        self.phone = phone
        self.email = email
        self.contact_person = contact_person
        self.user_inserted = user_inserted


def fill_client(id ,arr_client_name, arr_client_adress, arr_phone, arr_email, arr_contact_person, arr_user_inserted):
    col_client.drop()

    for client_name, client_adress, phone, email, contact_person, user_inserted in product(arr_client_name
            , arr_client_adress, arr_phone, arr_email, arr_contact_person, arr_user_inserted):

        client_account = Client(id, client_name, client_adress, phone, email, contact_person, user_inserted)
        client_account_dict = vars(client_account)
        x = col_client.insert_one(client_account_dict)
        id+=1

#fixme когда создастся общий __main__ убрать
fill_client(id ,arr_client_name, arr_client_adress, arr_phone, arr_email, arr_contact_person, arr_user_inserted)

#Закрытие конекта
client.close()
