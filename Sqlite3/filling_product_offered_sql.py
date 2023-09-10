import sqlite3
import random
import time
import sys


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

    list_size_in_gigabytes = sys.getsizeof(arr_offers) / (1024 ** 3)
    print(f"Размер списка в гигабайтах: {list_size_in_gigabytes} ГБ")

    time_start = time.time()
    cursor.executemany("INSERT INTO product_offered (product_id, task_id, units) VALUES (?, ?, ?)", arr_offers)
    con.commit()
    time_end = time.time()
    return list_size_in_gigabytes
    # print(f"Запись данных рекомендаций {time_end - time_start}")
