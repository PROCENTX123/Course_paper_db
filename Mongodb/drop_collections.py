from pymongo import MongoClient

def drop_collections():
    client = MongoClient("mongodb://localhost:27017/")
    mydb = client['course_paper']

    col_task = mydb["task"]
    col_task.drop()

    col_user_account = mydb["user_account"]
    col_user_account.drop()

    col_client = mydb["client"]
    col_client.drop()

