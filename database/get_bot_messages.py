import pymongo


def main(command):
    db_client = pymongo.MongoClient("mongodb://localhost:27017/")
    current_db = db_client["telegram_bot"]
    collection = current_db["bot_messages"]
    return collection.find_one({'cmd': command})


def main_by_u_id(command):
    db_client = pymongo.MongoClient("mongodb://localhost:27017/")
    current_db = db_client["telegram_bot"]
    collection = current_db["bot_messages"]
    return collection.find_one({'u_id': command})