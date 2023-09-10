import sqlite3
from itertools import product
import time
import sys

def get_user_inserted():
    # обязательный сетап открытия
    con = sqlite3.connect("C:/Users/user/DataGripProjects/Course_paper_sql/identifier.sqlite")
    cursor = con.cursor()

    cursor.execute('select id from user_account')
    user_id = cursor.fetchall()
    arr_user_inserted = [row[0] for row in user_id]

    cursor.close()
    con.close()

    return arr_user_inserted

def fill_client(id, arr_client_name, arr_client_adress, arr_phone, arr_email, arr_contact_person, arr_user_inserted):
    # обязательный сетап открытия
    con = sqlite3.connect("C:/Users/user/DataGripProjects/Course_paper_sql/identifier.sqlite")
    con.execute("Pragma foreign_keys = 1")
    cursor = con.cursor()

    arr_clients = []
    arr_pairs = []

    cursor.execute("""CREATE TABLE client
        (id integer primary key ,
        client_name varchar(255),
        client_adress varchar(255),
        phone varchar(64),
        email varchar(63),
        contact_person varchar(255),
        user_inserted integer,
        foreign key (user_inserted) references user_account(id)
        )""")
    con.commit()



    for client_name, client_adress, phone, email, contact_person, user_inserted in product(arr_client_name,
                arr_client_adress, arr_phone, arr_email, arr_contact_person, arr_user_inserted):
        client_account = (id, client_name, client_adress, phone, email, contact_person, user_inserted)
        arr_clients.append(client_account)
        arr_pairs.append((id, user_inserted))
        id+=1


    list_size_in_gigabytes = sys.getsizeof(arr_clients) / (1024 ** 3)
    print(f"Размер списка в гигабайтах: {list_size_in_gigabytes} ГБ")


    time_start = time.time()
    cursor.executemany("Insert into  client (id, client_name, client_adress, phone, email, contact_person, user_inserted)  values(?, ?, ?, ?, ?, ?, ?)", arr_clients)
    con.commit()
    time_end = time.time()
    # print(f"Запись данных клиентов {time_end - time_start}")
    return arr_pairs, list_size_in_gigabytes
