import random
import sqlite3

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


def fill_product_sold(arr_id_product, arr_task_for_sale, arr_units):
    # обязательный сетап открытия
    con = sqlite3.connect("C:/Users/user/DataGripProjects/Course_paper_sql/identifier.sqlite")
    cursor = con.cursor()

    arr_sales = []

    cursor.execute("""CREATE TABLE product_sold
        (id integer primary key autoincrement,
        id_product integer,
        id_task integer,
        units real,
        foreign key (id_product) references product(id),
        foreign key (id_task) references task(id)
        )""")
    con.commit()
    for id_task in arr_task_for_sale:
        id_product = random.choice(arr_id_product)
        units = random.choice(arr_units)
        sale = (id_product, id_task, units)
        arr_sales.append(sale)
    cursor.executemany("INSERT INTO product_sold (id_product, id_task, units) VALUES (?, ?, ?)", arr_sales)
    con.commit()
