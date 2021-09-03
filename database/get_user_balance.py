import pymongo


def main(u_id):
    db_client = pymongo.MongoClient("mongodb://localhost:27017/")
    current_db = db_client["telegram_bot"]
    collection = current_db["users"]
    return collection.find_one({'u_id': u_id})['balance']
