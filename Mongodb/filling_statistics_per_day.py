from pymongo import MongoClient



#открытие коннекта
client = MongoClient("mongodb://localhost:27017/")
mydb = client['course_paper']
col_statistic = mydb["statistic"]

class Statistic:
    def __init__(self, client_name, tasks, start_time, end_time, meetings, calls,  sales, offer, price_for_sale, price_for_offer, units):
        self.client_name = client_name
        self.tasks = tasks
        self.start_time = start_time
        self.end_time = end_time
        self.meetings = meetings
        self.calls = calls
        self.sales = sales
        self.offer = offer
        self.price_for_sale = price_for_sale
        self.price_for_offer = price_for_offer
        self.units = units

    def __dict__(self):
        return {
            "client_name": self.client_name,
            "tasks": self.tasks,
            "start_time": self.start_time,
            "end_time": self.end_time,
            "meetings": self.meetings,
            "calls": self.calls,
            "sales": self.sales,
            "offer": self.offer,
            "price_sale": self.price_for_sale,
            "price_offer": self.price_for_offer,
            "units": self.units
        }



def filling_statistic( task_dict, meeting_dict, call_dict, product_sold_dict, product_offered_dict):
    statistic_dict = {}
    for key_task, value_task in task_dict.items():
        # Инициализируем пустой словарь для каждого клиента
        statistic_dict.setdefault(value_task.client_name, {})

        for key_meeting, value_meeting in meeting_dict.items():
            if value_meeting.client_id == value_task.client_id and key_task == value_meeting.task_id:
                statistic = Statistic(value_task.client_name, key_task, value_meeting.start_time, value_meeting.end_time,
                                      key_meeting, None, None, None, None, None, None)
                col_statistic.insert_one(statistic.__dict__())

                statistic_dict[value_task.client_name][key_task] = (
                    value_task.client_id,
                    value_meeting.user_account_id,
                    value_meeting.start_time,
                    value_meeting.end_time
                )

        for key_call, value_call in call_dict.items():
            if value_call.client_id == value_task.client_id and key_task == value_call.task_id:
                statistic = Statistic(value_task.client_name, key_task, value_call.start_time, value_call.end_time,
                                      None, key_call, None, None, None, None, None)
                col_statistic.insert_one(statistic.__dict__())

                statistic_dict[value_task.client_name][key_task] = (
                    value_task.client_id,
                    value_call.user_account_id,
                    value_call.start_time,
                    value_call.end_time
                )
        for key_sold, value_sold in product_sold_dict.items():
            if value_sold.client_id == value_task.client_id and key_task == value_sold.task_id:
                statistic = Statistic(value_task.client_name, key_task, value_task.start_time, value_task.end_time,
                                      None, None, value_sold.id, None, value_sold.price, None, value_sold.units)
                col_statistic.insert_one(statistic.__dict__())

                statistic_dict[value_task.client_name][key_task] = (
                    value_task.client_id,
                    value_sold.product_id,
                    value_sold.price,
                    value_sold.units
                )
        for key_offer, value_offer in product_offered_dict.items():
            if value_offer.client_id == value_task.client_id and key_task == value_offer.task_id:
                statistic = Statistic(value_task.client_name, key_task, value_task.start_time, value_task.end_time,
                                      None, None, None, value_offer.id, None, value_offer.price, value_offer.units)
                col_statistic.insert_one(statistic.__dict__())
                statistic_dict[value_task.client_name][key_task] = (
                    value_task.client_id,
                    value_offer.product_id,
                    value_offer.price,
                    value_offer.units
                )
    return statistic_dict