import sqlite3
from itertools import product



def get_id_task_outcome():
    con = sqlite3.connect("C:/Users/user/DataGripProjects/Course_paper_sql/identifier.sqlite")
    con.execute("Pragma foreign_keys = 1")
    cursor = con.cursor()

    cursor.execute("select id from task_outcome")
    result = cursor.fetchall()
    arr_task_outcome = [row[0] for row in result]

    cursor.close()
    con.close()
    return arr_task_outcome

def fill_task(arr_client_and_user, arr_start_time,arr_end_time):
    con = sqlite3.connect("C:/Users/user/DataGripProjects/Course_paper_sql/identifier.sqlite")
    con.execute("Pragma foreign_keys = 1")
    cursor = con.cursor()

    arr_tasks = []
    arr_pairs_for_meeting = []
    arr_pairs_for_calls = []
    arr_for_sale = []
    arr_for_offered = []
    id = 1

    count_all_task = len(arr_client_and_user) * len(arr_start_time) * len(arr_end_time)

    cursor.execute("""CREATE TABLE task
        (
        id integer primary key,
        client_id integer,
        start_time timestamp,
        end_time timestamp,
        user_assigned integer,
        task_outcome_id integer default null,
        foreign key (client_id) references client(id)
        foreign key (user_assigned) references user_account(id)
        foreign key(task_outcome_id) references task_outcome(id)
        )
        """)
    con.commit()

    for client_and_user in arr_client_and_user:
        for start_time, end_time in product(arr_start_time, arr_end_time):
            task = (id, client_and_user[0], start_time, end_time, client_and_user[1])
            arr_tasks.append(task)
            if id > count_all_task * 0.25 and id <= count_all_task * 0.5:
                arr_pairs_for_calls.append((client_and_user[1], id))
            elif id > 0 and id <= count_all_task * 0.25:
                arr_pairs_for_meeting.append((client_and_user[1], id))
            elif id > count_all_task * 0.5 and id <= count_all_task * 0.75:
                arr_for_sale.append(id)
            elif id > count_all_task * 0.75 and id <=count_all_task:
                arr_for_offered.append(id)
            id+=1
    cursor.executemany("Insert into  task (id, client_id, start_time, end_time, user_assigned) values(?, ?, ?, ?, ?)", arr_tasks)
    con.commit()
    return arr_pairs_for_meeting, arr_pairs_for_calls, arr_for_sale, arr_for_offered







