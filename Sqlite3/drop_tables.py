import sqlite3
def drop_tables():
    con = sqlite3.connect("C:/Users/user/DataGripProjects/Course_paper_sql/identifier.sqlite")
    con.execute("Pragma foreign_keys = 1")
    cursor = con.cursor()

    table_name = "call"
    cursor.execute(f"Drop table if exists {table_name}")
    con.commit()

    table_name = "meeting"
    cursor.execute(f"Drop table if exists {table_name}")
    con.commit()

    table_name = "task"
    cursor.execute(f"Drop table if exists {table_name}")
    con.commit()


    table_name = "client"
    cursor.execute(f"Drop table if exists {table_name}")
    con.commit()

    table_name = "user_account"
    cursor.execute(f"Drop table if exists {table_name}")
    con.commit()