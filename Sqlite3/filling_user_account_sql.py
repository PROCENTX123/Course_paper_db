import sqlite3
from itertools import product
import time
import sys


def fill_user_account(arr_name, arr_lastname, arr_username, arr_passwords):
    # обязательный сетап открытия
    con = sqlite3.connect("C:/Users/user/DataGripProjects/Course_paper_sql/identifier.sqlite")
    cursor = con.cursor()

    arr_users = []

    cursor.execute("""CREATE TABLE user_account
        (id integer primary key autoincrement,
        first_name varchar(255),
        last_name varchar(255),
        user_name varchar(255),
        password varchar(200))""")
    con.commit()
    for name, lastname, username, password in product(arr_name, arr_lastname, arr_username, arr_passwords):
        user_account = (name, lastname, username, password)
        arr_users.append(user_account)

    list_size_in_gigabytes = sys.getsizeof(arr_users) / (1024 ** 3)
    print(f"Размер списка в гигабайтах: {list_size_in_gigabytes} ГБ")

    time_start = time.time()
    cursor.executemany("INSERT INTO user_account (first_name, last_name, user_name, password) VALUES (?, ?, ?, ?)", arr_users)
    con.commit()
    time_end = time.time()
    return list_size_in_gigabytes
    # print(f"Запись данных юзеров {time_end - time_start}")




