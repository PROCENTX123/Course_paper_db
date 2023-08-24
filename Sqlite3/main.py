import sqlite3
import datetime
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
    arr_client_name = ["MTC"]
    arr_client_adress = ["Курская 4а"]
    arr_phone = ["11111"]
    arr_email = ["romkagrigorev@mail.ru"]
    arr_contact_person = ["Vasiliy"]
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
    arr_units = [2]
    filling_product_sold_sql.fill_product_sold(arr_id_product, arr_for_sale, arr_units)


    #data
    arr_id_product = filling_product_offered_sql.get_product_id()
    arr_units = [1]
    filling_product_offered_sql.fill_product_offered(arr_id_product, arr_for_offered, arr_units)

    # сетап закрытия
    cursor.close()
    con.close()

