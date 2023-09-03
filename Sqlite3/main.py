import sqlite3
import datetime
import time

import drop_tables
import filling_user_account_sql
import filling_client_sql
import filling_task_sql
import filling_meeting_sql
import filling_call_sql
import filling_product_sql
import filling_product_sold_sql
import filling_product_offered_sql


if __name__=="__main__":
    # обязательный сетап открытия
    con = sqlite3.connect("C:/Users/user/DataGripProjects/Course_paper_sql/identifier.sqlite")
    con.execute("Pragma foreign_keys = 1")
    cursor = con.cursor()


    drop_tables.drop_tables()


    #data
    arr_name = ["Roman", "Ivan", "Vladimir", "Dmitriy", "Nikita"]
    arr_lastname = ["Grigorev", "Ivanov", "Petrov", "Sidorov", "X"]
    arr_username = ["Procent", "Lox", "MOx", "Bubaleh", "uxz"]
    arr_passwords = ["12345", "54321", "11111", "123", "00000"]
    filling_user_account_sql.fill_user_account(arr_name, arr_lastname, arr_username, arr_passwords)


    #data
    id = 1
    # 5 000 тасков
    # arr_client_name = ["BBC", "HBC"]
    # arr_client_adress = ["Курская 4а"]
    # arr_phone = ["11111"]
    # arr_email = ["romkagrigorev@mail.ru"]
    # arr_contact_person = ["Vasiliy"]

    # 120 000 тасков
    # arr_client_name = ["BBC", "HBC", "Rockstar", "Ponchiki"]
    # arr_client_adress = ["Курская 4а", "Василевская 16"]
    # arr_phone = ["11111", "22222", "33333"]
    # arr_email = ["romkagrigorev@mail.ru"]
    # arr_contact_person = ["Vasiliy", "Vanya"]

    # 675 000 тасков
    # arr_client_name = ["BBC", "Valve", "Rockstar", "Ponchiki", "StarBucks", "Leliki", "Boliki", "Navi", "VP", "TS"]
    # arr_client_adress = ["Курская 4а", "Василевская 16", "Тропическая 22"]
    # arr_phone = ["11111", "22222", "33333"]
    # arr_email = ["romkagrigorev@mail.ru"]
    # arr_contact_person = ["Vasiliy", "Vanya", "Tolya"]

    # 2 080 000 тасков
    # arr_client_name = ["BBC", "Valve", "Rockstar", "Ponchiki", "StarBucks", "Leliki", "Boliki", "Navi", "VP", "TS",
    #                    "HR", "Tundra", "5 озер"]
    # arr_client_adress = ["Курская 4а", "Василевская 16", "Тропическая 22", "Заводская 20Б"]
    # arr_phone = ["11111", "22222", "33333", "444444"]
    # arr_email = ["romkagrigorev@mail.ru"]
    # arr_contact_person = ["Vasiliy", "Vanya", "Tolya", "Zhenya"]

    # 3 200 000 тасков
    # arr_client_name = ["BBC", "Valve", "Rockstar", "Ponchiki", "StarBucks", "Leliki", "Boliki", "Navi", "VP", "TS",
    #                    "HR", "Tundra", "5 озер", "Балтика", "Охота", "Арсенал"]
    # arr_client_adress = ["Курская 4а", "Василевская 16", "Тропическая 22", "Заводская 20Б"]
    # arr_phone = ["11111", "22222", "33333", "444444", "555555"]
    # arr_email = ["romkagrigorev@mail.ru"]
    # arr_contact_person = ["Vasiliy", "Vanya", "Tolya", "Zhenya"]

    # 5 млн тасков
    # arr_client_name = ["BBC", "Valve", "Rockstar", "Ponchiki", "StarBucks", "Leliki", "Boliki", "Navi", "VP", "TS",
    #                    "HR", "Tundra", "5 озер", "Балтика", "Охота", "Арсенал"]
    # arr_client_adress = ["Курская 4а", "Василевская 16", "Тропическая 22", "Заводская 20Б", "Горопачи 15"]
    # arr_phone = ["11111", "22222", "33333", "444444", "55555"]
    # arr_email = ["romkagrigorev@mail.ru"]
    # arr_contact_person = ["Vasiliy", "Vanya", "Tolya", "Zhenya", "Kolya"]

    # 9 120 000 тасков
    # arr_client_name = ["BBC", "Valve", "Rockstar", "Ponchiki", "StarBucks", "Leliki", "Boliki", "Navi", "VP", "TS",
    #                    "HR", "Tundra", "5 озер", "Балтика", "Охота", "Арсенал", "DYW", "Тинькофф", "МТС"]
    # arr_client_adress = ["Курская 4а", "Василевская 16", "Тропическая 22", "Заводская 20Б", "Горопачи 15",
    #                      "Заводская 30", "Скобелевская 16", "Краснознаменская 20"]
    # arr_phone = ["11111", "22222", "33333", "444444", "55555", "6666666"]
    # arr_email = ["romkagrigorev@mail.ru"]
    # arr_contact_person = ["Vasiliy", "Vanya", "Tolya", "Zhenya"]

    # 13.2 млн тасков
    arr_client_name = ["BBC", "Valve", "Rockstar", "Ponchiki", "StarBucks", "Leliki", "Boliki", "Navi", "VP", "TS",
                       "HR", "Tundra", "5 озер", "Балтика", "Охота", "Арсенал", "DYW", "Тинькофф", "МТС", "Билайн",
                       "Мегафон", "Райфайзен"]
    arr_client_adress = ["Курская 4а", "Василевская 16", "Тропическая 22", "Заводская 20Б", "Горопачи 15",
                         "Заводская 30", "Скобелевская 16", "Краснознаменская 20"]
    arr_phone = ["11111", "22222", "33333", "444444", "55555", "6666666"]
    arr_email = ["romkagrigorev@mail.ru"]
    arr_contact_person = ["Vasiliy", "Vanya", "Tolya", "Zhenya", "Kolya"]
    arr_user_inserted = filling_client_sql.get_user_inserted()

    pair_client_user = filling_client_sql.fill_client(id, arr_client_name, arr_client_adress, arr_phone, arr_email, arr_contact_person, arr_user_inserted)


    #data
    arr_client_and_user = pair_client_user
    arr_start_time = [datetime.datetime(year=2023, month=8, day=18, hour=9, minute=00, second=00),
                      datetime.datetime(year=2023, month=8, day=18, hour=12, minute=00, second=00)]
    arr_end_time = [datetime.datetime(year=2023, month=8, day=18, hour=13, minute=00, second=00),
                    datetime.datetime(year=2023, month=8, day=18, hour=15, minute=00, second=00)]
    arr_task_outcome_id = filling_task_sql.get_id_task_outcome()



    #data
    arr_pair_for_meeting, arr_pair_for_call, arr_for_sale, arr_for_offered = filling_task_sql.fill_task(arr_client_and_user, arr_start_time, arr_end_time)
    arr_start_time_meeting = [datetime.datetime(year=2023, month=9, day=19, hour=10, minute=00, second=00)]
    arr_end_time_meeting = [datetime.datetime(year=2023, month=9, day=19, hour=14, minute=00, second=00)]

    filling_meeting_sql.fill_meeting(arr_pair_for_meeting, arr_start_time_meeting, arr_end_time_meeting)

    #data
    arr_start_time_call = [datetime.datetime(year=2023, month=9, day=25, hour=9, minute=00, second=00)]
    arr_end_time_call = [datetime.datetime(year=2023, month=9, day=25, hour=12, minute=00, second=00)]
    filling_call_sql.fill_call(arr_pair_for_call, arr_start_time_call, arr_end_time_call)



    #data
    product_name = ["Стекло", "Гантели", "Машина"]
    unit = [2, 3, 4, 5]
    price_per_unit = [100, 200, 300]
    filling_product_sql.fill_product(product_name, unit, price_per_unit)


    #data
    arr_id_product = filling_product_sold_sql.get_product_id()
    arr_units = [2, 3, 4, 5]
    filling_product_sold_sql.fill_product_sold(arr_id_product, arr_for_sale, arr_units)


    #data
    arr_id_product = filling_product_offered_sql.get_product_id()
    arr_units = [2, 3, 4, 5]
    filling_product_offered_sql.fill_product_offered(arr_id_product, arr_for_offered, arr_units)

    # индексы для запроса с такой то даты по такую то дату
    # cursor.execute("CREATE INDEX idx_task_client_id ON task (client_id)")
    # cursor.execute("create index idx_product_sold_task_id on product_sold(task_id)")
    # cursor.execute("create index idx_client_name on client (client_name)")
    # cursor.execute("create index idx_product_sold_product_id on product_sold(product_id)")
    # cursor.execute("create index idx_task_start_time on task(start_time)")
    # cursor.execute("create index idx_task_end_time on task(end_time)")

    #индексы для запроса на всю статистику
    cursor.execute("CREATE INDEX idx_task_client_id ON task (client_id)")
    cursor.execute("create index idx_meeting_task_id on meeting(task_id)")
    cursor.execute("create index idx_call_task_id on call(task_id)")
    cursor.execute("create index idx_product_sold_task_id on product_sold(task_id)")
    cursor.execute("create index idx_product_offer_task_id on product_offered(task_id)")
    cursor.execute("create index idx_client_name on client (client_name)")

    #индекс для 3-его запроса
    # cursor.execute("CREATE INDEX idx_task_client_id ON task (client_id)")
    # cursor.execute("create index idx_product_sold_task_id on product_sold(task_id)")
    # cursor.execute("create index idx_product_sold_product_id on product_sold(product_id)")
    # cursor.execute("create index idx_product_units on product(unit)")
    # cursor.execute("create index idx_product_price_per_unit on product(price_per_unit)")

    #индекс для 4-го запроса
    # cursor.execute("CREATE INDEX idx_task_client_id ON task (client_id)")
    # cursor.execute("create index idx_product_sold_task_id on product_sold(task_id)")
    # cursor.execute("create index idx_product_sold_product_id on product_sold(product_id)")
    # cursor.execute("CREATE INDEX idx_product_name ON product (product_name)")
    # cursor.execute("CREATE INDEX idx_product_id_count_sold ON product_sold (product_id, task_id)")

    con.commit()

    time_check_start = time.time()
    cursor.execute("""
    select client.client_name,
       count(distinct task.id) as total_tasks,
       count(distinct call.id) as total_calls,
       count(distinct meeting.id) as total_meeting,
       count(distinct product_sold.id) as total_sold_product,
       count(distinct product_offered.id) as total_product_offered
    from client
    join task on client.id = task.client_id
    left join call on  task.id = CALL.task_id
    left join meeting on task.id = meeting.task_id
    left join product_sold  on task.id = product_sold.task_id
    left join product_offered on task.id = product_offered.task_id
    group by client.client_name;
    """)
    time_check_end = time.time()
    # print(time_check_end - time_check_start)

    # results = cursor.fetchall()
    # for row in results:
    #     print(row)

    # сетап закрытия
    cursor.close()
    con.close()

