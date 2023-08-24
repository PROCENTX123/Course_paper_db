import sqlite3
from itertools import product

#data
arr_client_name = ["MTC"]
arr_client_adress = ["Курская 4а"]
arr_phone = ["11111"]
arr_email = ["romkagrigorev@mail.ru"]
arr_contact_person = ["Vasiliy"]
#fixme это foreign key, поправить это место потому что может встать рандомный id который крашнется
arr_user_inserted = [1, 2]
id = 1
arr_clients = []

#открытие коннекта
con = sqlite3.connect("/home/roman/DataGripProjects/Couse_paper/identifier.sqlite")
#поддержка foreign key
con.execute("Pragma foreign_keys = 1")
#открытие курсора
cursor = con.cursor()

#fixme когда создастся общий генератор данных вызывать эту функцию там
def fill_client(id ,arr_client_name, arr_client_adress, arr_phone, arr_email, arr_contact_person, arr_user_inserted):
    table_name = "client"
    cursor.execute(f"Drop table {table_name}")
    con.commit()

    cursor.execute("""CREATE TABLE client
        (id integer primary key,
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
        id+=1
    cursor.executemany("Insert into  client values(?, ?, ?, ?, ?, ?, ?)", arr_clients)
    con.commit()

fill_client(id, arr_client_name, arr_client_adress, arr_phone, arr_email, arr_contact_person, arr_user_inserted)

#закрытие курсора
cursor.close()

#закрытие подключения
con.close()
