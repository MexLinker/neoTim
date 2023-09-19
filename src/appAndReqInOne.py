# -*- coding: utf-8 -*-
"""
Created on Wed Jan 11 11:00:43 2023

@author: 26440
"""

from pymongo import MongoClient
from bson.json_util import dumps
# from bson.json_util import loads

from flask import Flask

# from markupsafe import escape

from flask import request

# import connect

app = Flask(__name__)


CONNECTION_STRING = "mongodb+srv://max:Maxmax123@todocluster.h6wo1.mongodb.net/?retryWrites=true&w=majority"

client = MongoClient(CONNECTION_STRING)

db = client.get_database("todoList")


colUsergao = db.get_collection('userGaoList')



def connectFunc(method, content, col):
    
    returnMessage = 'the whole function did nothing'
    
    # CONNECTION_STRING = "mongodb+srv://max:Maxmax123@todocluster.h6wo1.mongodb.net/?retryWrites=true&w=majority"
    
    # client = MongoClient(CONNECTION_STRING)
    
    # db = client.get_database("todoList")

    
    # colUsergao = db.get_collection('userGaoList')
    
   
    
    def addOne(theContentToAdd):
        
        # theContentToAdd
        
        record = {"method": 1, "data": {"date": 2019, "tag": "work", "content": theContentToAdd, "done": "false"}}
        
        colUsergao.insert_one(record)
        
        strstrstrNew = """[{"_id": {"$oid": "6268c6faf4c2fd742ce5be9d"}, "method": 1, "data": {"date": 2019, "tag": "work", "content": "inserted successfully", "done": "false"}}]"""
        
        return strstrstrNew
        
    def findAll():
        
        cursor = col.find()

        dataJsonString = dumps(cursor)

        # dataList = loads(dataJsonString)
        
        return dataJsonString
    
    def findOne():
        
        one = col.aggregate( [
            {"$sample": { "size" : 1} },
        ] )
        
        oneD = dumps(one)
        
        return oneD
    
    def deleteOne(theContentToDel):
        
        # col.find_one_and_delete(filter, kwargs)
        
        # record = { "data": {"conetnt" : theContentToDel} }

        
        # col.find_one_and_delete(record)
        
        record = { "data.content" : theContentToDel } 

         
        # returnM = colUsergao.find_one_and_delete(record)

        returnMDO = colUsergao.delete_one(record)
        
        strstrstrNew = """[{"_id": {"$oid": "6268c6faf4c2fd742ce5be9d"}, "method": 1, "data": {"date": 2019, "tag": "work", "content": "delete succeessflully", "done": "false"}}]"""
        
        
        return strstrstrNew
    
   
    
    if method == 'inputContent':
        returnMessage = addOne(content)
    
    if method == 'retrieveAllContent':    
        returnMessage = findAll()
    
    if method == 'retrieveOneContent':    
        returnMessage = findOne()
    
    if method == 'deleteOneContent':    
        returnMessage = deleteOne(content)
        

    # client.close()
    
    return returnMessage




@app.route('/timRecieve', methods=['POST', 'GET'])
def timRecieve():
    if request.method == 'POST':
        # print("req method is POST ")
        
        print(request.form['timMethod'])
        # print(request.form['content'])
        
        timMethod = request.form['timMethod']
        timContent = request.form['content']
        
        
        contentToReturn = connectFunc(timMethod, timContent, colUsergao)
        
        print(contentToReturn)
        
        return contentToReturn
    
    
    
    if request.method == 'GET':
        
        timMethod = request.args['timMethod']
        
        timContent = request.args['content']
        
        contentToReturn = connectFunc(timMethod, 1, colUsergao)
        
        return  contentToReturn
     




























