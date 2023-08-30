from pymongo import MongoClient
from itertools import product
from tqdm import tqdm


#открытие коннекта
client = MongoClient("mongodb://localhost:27017/")
mydb = client['course_paper']
col_client = mydb["client"]
col_user_account = mydb["user_account"]


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
            "user_inserted": self.user_inserted,
            "name_lastname_user": self._name_lastname_user_inserted
        }
    def to_dict(self):
        return self.__dict__()

def get_user_inserted():
    collection = mydb["user_account"]
    user_inserted = collection.distinct("id")
    return user_inserted


def fill_client(arr_client_name, arr_client_adress, arr_phone, arr_email, arr_contact_person, arr_user_inserted, user_dict):
    arr_pairs = []
    client_dict = {}
    arr_client_doc = []

    id = 1
    total_items = len(arr_client_name) * len(arr_client_adress) * len(arr_phone) * len(arr_email) * len(arr_contact_person) * len(arr_user_inserted)

    with tqdm(total=total_items, desc="Filling client") as pbar:
        for client_name, client_adress, phone, email, contact_person, user_inserted in product(arr_client_name
                , arr_client_adress, arr_phone, arr_email, arr_contact_person, arr_user_inserted):

            # target_user_id = user_inserted
            # pipeline = [
            #     {"$match": {"id": target_user_id}},
            #     {"$project": {"name_lastname_user": 1}}
            # ]
            # doc_user = mydb['user_account'].aggregate(pipeline)
            # doc = doc_user.next()
            # name_lastname_user_inserted = doc["name_lastname_user"]

            name_lastname_user_inserted = user_dict[user_inserted].name_lastname_user


            client_account = Client(id, client_name, client_adress, phone, email, contact_person, user_inserted, name_lastname_user_inserted)
            arr_client_doc.append(client_account.to_dict())

            client_dict[id] = client_account
            arr_pairs.append((id, user_inserted))
            id+=1

            pbar.update(1)
    col_client.insert_many(arr_client_doc)
    print("Client completed")
    return arr_pairs, client_dict


## 30 000 клиентов 7 секунд
