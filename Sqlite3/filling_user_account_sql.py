import sqlite3
from itertools import product


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
    cursor.executemany("INSERT INTO user_account (first_name, last_name, user_name, password) VALUES (?, ?, ?, ?)", arr_users)
    con.commit()




