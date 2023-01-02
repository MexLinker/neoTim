# -*- coding: utf-8 -*-
"""
Created on Sat Dec 31 12:20:29 2022

@author: 26440
"""

from pymongo import MongoClient

CONNECTION_STRING = "mongodb+srv://max:Maxmax123@todocluster.h6wo1.mongodb.net/?retryWrites=true&w=majority"

client = MongoClient(CONNECTION_STRING)

db = client.get_database("todoList")

collectionNames = db.list_collection_names()

dbUsergao = db.get_collection('userGaoList')

jjson = dbUsergao.find_one({'method': 1})

id = jjson.get("_id")

idItem = dbUsergao.find_one(id)

boolerer = idItem == jjson

print(boolerer)

print(idItem)

print(type(idItem))

print(idItem["_id"])

print(idItem["data"]["content"])

# {'_id': ObjectId('618f73a870e67e5bfb0c6141'), 'method': 1, 'data': {'date': 2019, 'tag': 'work', 'content': 'tim means i want to treasure my time', 'done': 'false'}}

# print(thisdict["brand"])


# almost done
