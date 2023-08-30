import filling_user_account_nosql
import filling_client_nosql
import filling_task_nosql
import filling_call_nosql
import filling_meeting_nosql
import filling_product_nosql
import filling_product_sold_nosql
import filling_product_offered_nosql
import filling_statistics_per_day
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

    user_dict = filling_user_account_nosql.fill_user_account(arr_name, arr_lastname, arr_username, arr_passwords)
    # for key, value in user_dict.items():
    #     print(f"ID: {key}, Name: {value.first_name}, Age: {value.last_name}, Name_lastname: {value._name_lastname_user}")


    # 5 000 тасков
    # arr_client_name = ["BBC", "HBC"]
    # arr_client_adress = ["Курская 4а"]
    # arr_phone = ["11111"]
    # arr_email = ["romkagrigorev@mail.ru"]
    # arr_contact_person = ["Vasiliy"]

    #120 000 тасков
    # arr_client_name = ["BBC", "HBC", "Rockstar", "Ponchiki"]
    # arr_client_adress = ["Курская 4а", "Василевская 16"]
    # arr_phone = ["11111", "22222", "33333"]
    # arr_email = ["romkagrigorev@mail.ru"]
    # arr_contact_person = ["Vasiliy", "Vanya"]

    #5 млн тасков
    arr_client_name = ["BBC", "Valve", "Rockstar", "Ponchiki", "StarBucks", "Leliki", "Boliki", "Navi", "VP", "TS",
                       "HR", "Tundra", "5 озер", "Балтика", "Охота", "Арсенал"]
    arr_client_adress = ["Курская 4а", "Василевская 16", "Тропическая 22", "Заводская 20Б", "Горопачи 15"]
    arr_phone = ["11111", "22222", "33333", "444444", "55555"]
    arr_email = ["romkagrigorev@mail.ru"]
    arr_contact_person = ["Vasiliy", "Vanya", "Tolya", "Zhenya", "Kolya"]

    arr_user_inserted = filling_client_nosql.get_user_inserted()


    pair_client_user, client_dict = filling_client_nosql.fill_client(arr_client_name, arr_client_adress, arr_phone,
                                                                     arr_email, arr_contact_person, arr_user_inserted,
                                                                     user_dict)

    # data
    arr_start_time = [datetime.datetime(year=2023, month=8, day=18, hour=9, minute=00, second=00),
                      datetime.datetime(year=2023, month=8, day=18, hour=12, minute=00, second=00)]
    arr_end_time = [datetime.datetime(year=2023, month=8, day=18, hour=13, minute=00, second=00),
                    datetime.datetime(year=2023, month=8, day=18, hour=15, minute=00, second=00)]

    task_dict, arr_pair_for_meeting, arr_pair_for_call, arr_for_sale, arr_for_offered = filling_task_nosql.fill_task(
        client_dict, arr_start_time, arr_end_time)

    #data
    arr_start_time_meeting = [datetime.datetime(year=2023, month=9, day=19, hour=10, minute=00, second=00)]
    arr_end_time_meeting = [datetime.datetime(year=2023, month=9, day=19, hour=14, minute=00, second=00)]
    meeting_list = filling_meeting_nosql.fill_meeting(task_dict, arr_pair_for_meeting, arr_start_time_meeting,
                                                      arr_end_time_meeting)

    #data
    # print(len(arr_pair_for_call))
    arr_start_time_call = [datetime.datetime(year=2023, month=9, day=25, hour=9, minute=00, second=00)]
    arr_end_time_call = [datetime.datetime(year=2023, month=9, day=25, hour=12, minute=00, second=00)]
    calls_list = filling_call_nosql.fill_call(task_dict, arr_pair_for_call, arr_start_time_call, arr_end_time_call)

    #data
    product_name = ["Стекло", "Гантели", "Машина"]
    unit = [2, 3, 4, 5]
    price_per_unit = [100, 200, 300]
    unit_in_stock = [10]
    product_list = filling_product_nosql.fill_product(product_name, unit, price_per_unit, unit_in_stock)


    product_sold_list = filling_product_sold_nosql.fill_product_sold(task_dict, arr_for_sale, product_list)

    product_offered_list = filling_product_offered_nosql.fill_product_offered(task_dict, arr_for_offered, product_list)



    statistic = filling_statistics_per_day.filling_statistic(meeting_list, calls_list, product_sold_list, product_offered_list)

    client.close()