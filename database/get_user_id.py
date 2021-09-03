import pymongo
import database.create_user_profile as create_user_profile


def main(message):
    db_client = pymongo.MongoClient("mongodb://localhost:27017/")
    current_db = db_client["telegram_bot"]
    collection = current_db["users"]
    for _ in collection.find({}, {'u_id': message.chat.id}):
        return message.chat.id
    return create_user_profile.main(message)
