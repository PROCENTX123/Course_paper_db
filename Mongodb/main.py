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

    user_dict = filling_user_account_nosql.fill_user_account(id, arr_name, arr_lastname, arr_username, arr_passwords)
    # for key, value in user_dict.items():
    #     print(f"ID: {key}, Name: {value.first_name}, Age: {value.last_name}, Name_lastname: {value._name_lastname_user}")


    #data
    arr_client_name = ["BBC", "HBC"]
    arr_client_adress = ["Курская 4а"]
    arr_phone = ["11111"]
    arr_email = ["romkagrigorev@mail.ru"]
    arr_contact_person = ["Vasiliy"]
    arr_user_inserted = filling_client_nosql.get_user_inserted()
    id = 1

    pair_client_user, client_dict = filling_client_nosql.fill_client(id, arr_client_name, arr_client_adress, arr_phone,
                                                                     arr_email, arr_contact_person, arr_user_inserted,
                                                                     user_dict)
    # for key, value in client_dict.items():
    #     print(f"ID: {key}, Name: {value._name_lastname_user_inserted}, iserted_id:{value.user_inserted}")


    # data
    arr_start_time = [datetime.datetime(year=2023, month=8, day=18, hour=9, minute=00, second=00),
                      datetime.datetime(year=2023, month=8, day=18, hour=12, minute=00, second=00)]
    arr_end_time = [datetime.datetime(year=2023, month=8, day=18, hour=13, minute=00, second=00),
                    datetime.datetime(year=2023, month=8, day=18, hour=15, minute=00, second=00)]

    task_dict, arr_pair_for_meeting, arr_pair_for_call, arr_for_sale, arr_for_offered = filling_task_nosql.fill_task(
        client_dict, arr_start_time, arr_end_time)

    # print(arr_pair_for_meeting)
    # print(arr_pair_for_call)
    # print(arr_for_sale)
    # print(arr_for_offered)

    client.close()