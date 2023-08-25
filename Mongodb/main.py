import filling_user_account_nosql
import filling_client_nosql
import filling_task_nosql
import drop_collections
import datetime
from pymongo import MongoClient

if __name__ == "__main__":
    # открытие коннекта
    client = MongoClient("mongodb://localhost:27017/")
    mydb = client['course_paper']

    drop_collections.drop_collections()


    #data
    arr_name = ["Roman", "Ivan", "Vladimir", "Dmitriy", "Nikita"]
    arr_lastname = ["Grigorev", "Ivanov", "Petrov", "Sidorov", "X"]
    arr_username = ["Procent", "Lox", "MOx", "Bubaleh", "uxz"]
    arr_passwords = ["12345", "54321", "11111", "123", "00000"]
    id = 1

    filling_user_account_nosql.fill_user_account(id, arr_name, arr_lastname, arr_username, arr_passwords)


    #data
    arr_client_name = ["BBC", "HBC"]
    arr_client_adress = ["Курская 4а"]
    arr_phone = ["11111"]
    arr_email = ["romkagrigorev@mail.ru"]
    arr_contact_person = ["Vasiliy"]
    arr_user_inserted = filling_client_nosql.get_user_inserted()
    id = 1

    pair_client_user = filling_client_nosql.fill_client(id ,arr_client_name, arr_client_adress, arr_phone, arr_email, arr_contact_person, arr_user_inserted)

    # data
    arr_client_and_user = pair_client_user
    arr_client_name = filling_task_nosql.get_client_name()
    arr_user_name_lastname = filling_task_nosql.get_name_lastname_user()
    arr_start_time = [datetime.datetime(year=2023, month=8, day=18, hour=9, minute=00, second=00),
                      datetime.datetime(year=2023, month=8, day=18, hour=12, minute=00, second=00)]
    arr_end_time = [datetime.datetime(year=2023, month=8, day=18, hour=13, minute=00, second=00),
                    datetime.datetime(year=2023, month=8, day=18, hour=15, minute=00, second=00)]
    #fixme поправить этот момент количество arr_user_name_lastname меньше чем остальных
    print(len(arr_client_name))
    print(len(arr_user_name_lastname))
    print(len(arr_client_and_user))

    arr_pair_for_meeting, arr_pair_for_call, arr_for_sale, arr_for_offered = filling_task_nosql.fill_task(arr_client_name, arr_user_name_lastname, arr_client_and_user, arr_start_time, arr_end_time)


    client.close()