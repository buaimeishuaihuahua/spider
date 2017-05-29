# coding=utf-8
from flask import Flask
from flask import render_template
from pymongo import MongoClient
import json
app = Flask(__name__)


@app.route('/', methods=['GET'])
def get_voice():
    client = MongoClient('127.0.0.1', 27017)
    db = client.zhongwei
    collection = db.li
    data_list = []
    for item in collection.find():
        item.pop('_id')
        data_list.append(json.dumps(item))
    return render_template('index.html', data_list=data_list)


if __name__ == '__main__':
    app.debug = True
    app.run()







