# -*- coding: utf-8 -*-
"""
Created on Wed Jan 11 11:00:43 2023

@author: 26440
"""

from pymongo import MongoClient
from bson.json_util import dumps

from flask import Flask, request, jsonify

app = Flask(__name__)


CONNECTION_STRING = "mongodb+srv://max:Maxmax123@todocluster.h6wo1.mongodb.net/?retryWrites=true&w=majority"

client = MongoClient(CONNECTION_STRING)
db = client.get_database("todoList")
colUsergao = db.get_collection('userGaoList')


def connectFunc(method, content, col):
    returnMessage = 'the whole function did nothing'

    def addOne(theContentToAdd):
        record = {"method": 1, "data": {"date": 2019, "tag": "work", "content": theContentToAdd, "done": "false"}}
        col.insert_one(record)
        return dumps(record)

    def findAll():
        cursor = col.find()
        return dumps(list(cursor))

    def findOne():
        one = list(col.aggregate([{"$sample": {"size": 1}}]))
        return dumps(one)

    def deleteOne(theContentToDel):
        record = {"data.content": theContentToDel}
        col.delete_one(record)
        return dumps({"msg": "delete successfully"})

    if method == 'inputContent':
        returnMessage = addOne(content)
    elif method == 'retrieveAllContent':
        returnMessage = findAll()
    elif method == 'retrieveOneContent':
        returnMessage = findOne()
    elif method == 'deleteOneContent':
        returnMessage = deleteOne(content)

    return returnMessage


@app.route('/timRecieve', methods=['POST', 'GET'])
def timRecieve():
    try:
        if request.method == 'POST':
            timMethod = request.form['timMethod']
            timContent = request.form['content']
            contentToReturn = connectFunc(timMethod, timContent, colUsergao)
            return contentToReturn

        if request.method == 'GET':
            timMethod = request.args['timMethod']
            timContent = request.args['content']
            contentToReturn = connectFunc(timMethod, timContent, colUsergao)
            return contentToReturn
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)

