import sqlite3
from itertools import product

#data
arr_name = ["Roman", "Ivan", "Vladimir", "Dmitriy", "Nikita"]
arr_lastname = ["Grigorev", "Ivanov", "Petrov", "Sidorov", "X"]
arr_username = ["Procent", "Lox", "MOx", "Bubaleh", "uxz"]
arr_passwords = ["12345", "54321", "11111", "123", "00000"]
id = 1
arr_users = []

#открытие коннекта
con = sqlite3.connect("/home/roman/DataGripProjects/Couse_paper/identifier.sqlite")
#открытие курсора
cursor = con.cursor()

#fixme когда создастся общий генератор данных вызывать эту функцию там
def fill_user_account(id ,arr_name, arr_lastname, arr_username, arr_passwords):
    table_name = "user_account"
    cursor.execute(f"Drop table {table_name}")
    con.commit()

    cursor.execute("""CREATE TABLE user_account
        (id integer primary key,
        first_name varchar(255),
        last_name varchar(255),
        user_name varchar(255),
        password varchar(200))""")
    con.commit()

    for name, lastname, username, password in product(arr_name, arr_lastname, arr_username, arr_passwords):
        user_account = (id, name, lastname, username, password)
        arr_users.append(user_account)
        id+=1
    cursor.executemany("Insert into  user_account values(?, ?, ?, ?, ?)", arr_users)
    con.commit()

fill_user_account(id, arr_name, arr_lastname, arr_username, arr_passwords)

#закрытие курсора
cursor.close()
#закрытие подключения
con.close()
