from pymongo import MongoClient
from itertools import product


#открытие коннекта
client = MongoClient("mongodb://localhost:27017/")
mydb = client['course_paper']
col_client = mydb["client"]

class Client:
    def __init__(self, id, client_name, client_adress, phone, email, contact_person, user_inserted, name_lastname_user):
        self.id = id
        self.client_name = client_name
        self.client_adress = client_adress
        self.phone = phone
        self.email = email
        self.contact_person = contact_person
        self.user_inserted = user_inserted
        self._name_lastname_user_inserted = name_lastname_user

    def __dict__(self):
        return {
            "id": self.id,
            "client_name": self.client_name,
            "client_adress": self.client_adress,
            "phone": self.phone,
            "email": self.email,
            "contact_person": self.contact_person,
            "user_inserted": self.user_inserted
        }

def get_user_inserted():
    collection = mydb["user_account"]
    user_inserted = collection.distinct("id")
    return user_inserted


def fill_client(id ,arr_client_name, arr_client_adress, arr_phone, arr_email, arr_contact_person, arr_user_inserted, user_dict):
    arr_pairs = []
    client_dict = {}

    for client_name, client_adress, phone, email, contact_person, user_inserted in product(arr_client_name
            , arr_client_adress, arr_phone, arr_email, arr_contact_person, arr_user_inserted):

        name_lastname_user_inserted = user_dict[user_inserted]._name_lastname_user


        client_account = Client(id, client_name, client_adress, phone, email, contact_person, user_inserted, name_lastname_user_inserted)
        col_client.insert_one(client_account.__dict__())

        client_dict[id] = client_account
        arr_pairs.append((id, user_inserted))
        id+=1
    return arr_pairs, client_dict

