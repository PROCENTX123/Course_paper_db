import sqlite3
from itertools import product

#fixme доработать этот модуль

# data
arr_outcome_text = ["norm", "ploho"]
arr_completed_successfully = [True, False]
id = 1
arr_call_outcome = []

# открытие коннекта
con = sqlite3.connect("C:/Users/user/DataGripProjects/Course_paper_sql/identifier.sqlite")
# открытие курсора
cursor = con.cursor()

# fixme когда создастся общий генератор данных вызывать эту функцию там
def fill_call_outcome(id, outcome_text, completed_successfully):
    table_name = "call_outcome"
    cursor.execute(f"Drop table if exists {table_name}")
    con.commit()

    cursor.execute("""CREATE TABLE call_outcome
        (
        id integer primary key,
        outcome_text varchar(255),
        completed_successfully boolean
        )
        """)
    con.commit()

    for outcome_text, completed_successfully in product(arr_outcome_text, completed_successfully):
        call_outcome = (id, outcome_text, completed_successfully)
        arr_call_outcome.append(call_outcome)
        id += 1
    cursor.executemany("Insert into  call_outcome values(?, ?, ?)", arr_call_outcome)
    con.commit()


fill_call_outcome(id, arr_outcome_text, arr_completed_successfully)

# закрытие курсора
cursor.close()
# закрытие подключения
con.close()