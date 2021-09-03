import pymongo
from flask import Flask, render_template

app = Flask(__name__)


def main():
    db_client = pymongo.MongoClient("mongodb://localhost:27017/")
    current_db = db_client["telegram_bot"]
    collection = current_db["bot_messages"]
    cursor = collection.find({})
    sp = []
    idx = 0
    for document in cursor:
        if 'cmd' not in document.keys():
            document['cmd'] = '-'
        document['idx'] = idx
        sp.append(document)
        idx += 1
    return sp


@app.route("/")
def hello_world():
    return render_template('index.html', sp=main())


if __name__ == '__main__':
    app.run(host="127.0.0.1", port=8000, debug=True)