import sqlite3
from itertools import product



def get_id_call_outcome():
    con = sqlite3.connect("C:/Users/user/DataGripProjects/Course_paper_sql/identifier.sqlite")
    con.execute("Pragma foreign_keys = 1")
    cursor = con.cursor()

    cursor.execute("select id from call_outcome")
    result = cursor.fetchall()
    arr_call_outcome = [row[0] for row in result]

    cursor.close()
    con.close()
    return arr_call_outcome

def fill_call(pair_user_task, arr_start_time, arr_end_time):
    con = sqlite3.connect("C:/Users/user/DataGripProjects/Course_paper_sql/identifier.sqlite")
    con.execute("Pragma foreign_keys = 1")
    cursor = con.cursor()

    arr_calls = []
    id = 1


    cursor.execute("""CREATE TABLE call
        (
        id integer primary key,
        user_account_id integer,
        task_id integer,
        start_time timestamp,
        end_time timestamp,
        call_outcome_id integer default null,
        foreign key (user_account_id) references user_account(id)
        foreign key (task_id) references task(id)
        foreign key(call_outcome_id) references call_outcome(id)
        )
        """)
    con.commit()

    for user_and_task in pair_user_task:
        for start_time, end_time in product(arr_start_time, arr_end_time):
            call = (id, user_and_task[0], user_and_task[1], start_time, end_time)
            arr_calls.append(call)
            id+=1
    cursor.executemany("Insert into  call (id, user_account_id, task_id, start_time, end_time) values(?, ?, ?, ?, ?)", arr_calls)
    con.commit()
