import sqlite3
from itertools import product


def fill_product(arr_product_name, arr_unit, arr_price_per_unit):
    # обязательный сетап открытия
    con = sqlite3.connect("C:/Users/user/DataGripProjects/Course_paper_sql/identifier.sqlite")
    cursor = con.cursor()

    arr_products = []

    cursor.execute("""CREATE TABLE product
        (id integer primary key autoincrement,
        product_name varchar(255),
        unit integer,
        price_per_unit real
        )""")
    con.commit()
    for product_name, unit, price_per_unit in product(arr_product_name, arr_unit, arr_price_per_unit):
        item = (product_name, unit, price_per_unit)
        arr_products.append(item)
    cursor.executemany("INSERT INTO product (product_name, unit, price_per_unit) VALUES (?, ?, ?)", arr_products)
    con.commit()
