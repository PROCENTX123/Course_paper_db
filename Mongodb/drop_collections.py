from pymongo import MongoClient

def drop_collections():
    client = MongoClient("mongodb://localhost:27017/")
    mydb = client['course_paper']

    col_meet = mydb["meeting"]
    col_meet.drop()

    col_call = mydb["call"]
    col_call.drop()

    col_task = mydb["task"]
    col_task.drop()

    col_sold = mydb["product_sold"]
    col_sold.drop()

    col_statistic = mydb["statistic"]
    col_statistic.drop()

    col_offer = mydb["product_offered"]
    col_offer.drop()

    col_product = mydb["product"]
    col_product.drop()

    col_user_account = mydb["user_account"]
    col_user_account.drop()

    col_client = mydb["client"]
    col_client.drop()

