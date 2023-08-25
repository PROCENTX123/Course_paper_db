import sqlite3
import random


def get_product_id():
    # обязательный сетап открытия
    con = sqlite3.connect("C:/Users/user/DataGripProjects/Course_paper_sql/identifier.sqlite")
    cursor = con.cursor()

    cursor.execute('select id from product')
    item = cursor.fetchall()
    arr_id_product = [row[0] for row in item]

    cursor.close()
    con.close()

    return arr_id_product


def fill_product_offered(arr_id_product, arr_task_for_offered, arr_units):
    # обязательный сетап открытия
    con = sqlite3.connect("C:/Users/user/DataGripProjects/Course_paper_sql/identifier.sqlite")
    cursor = con.cursor()

    arr_offers = []

    cursor.execute("""CREATE TABLE product_offered
        (id integer primary key autoincrement,
        product_id integer,
        task_id integer,
        units real,
        foreign key (product_id) references product(id),
        foreign key (task_id) references task(id)
        )""")
    con.commit()
    for id_task in arr_task_for_offered:
        id_product = random.choice(arr_id_product)
        units = random.choice(arr_units)
        offer = (id_product, id_task, units)
        arr_offers.append(offer)
    cursor.executemany("INSERT INTO product_offered (product_id, task_id, units) VALUES (?, ?, ?)", arr_offers)
    con.commit()
