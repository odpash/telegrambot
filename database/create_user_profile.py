import pymongo


def main(message):
    db_client = pymongo.MongoClient("mongodb://localhost:27017/")
    current_db = db_client["telegram_bot"]
    collection = current_db["users"]
    collection.insert_one({'u_id': message.chat.id, 'balance': 0})
    return message.chat.id
