
# =============================================================================
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 31 12:20:29 2022

@author: 26440
"""

from pymongo import MongoClient
from bson.json_util import dumps
from bson.json_util import loads



def connectFunc(method, content):
    
    returnMessage = 'the whole function did nothing'
    
    CONNECTION_STRING = "mongodb+srv://max:Maxmax123@todocluster.h6wo1.mongodb.net/?retryWrites=true&w=majority"
    
    client = MongoClient(CONNECTION_STRING)
    
    db = client.get_database("todoList")

    
    colUsergao = db.get_collection('userGaoList')
    
   
    # the old addOne made a bug
    # def addOne(theContentToAdd):
        
    #     # theContentToAdd
        
    #     # colUsergao.insert_one()
        
    #     return 'this is add one'

    def addOne(theContentToAdd):

        record = {"method": 1, "data": {"date": 2019, "tag": "work", "content": theContentToAdd, "done": "false"}}

        colUsergao.insert_one(record)

        strstrstrNew = """[{"_id": {"$oid": "6268c6faf4c2fd742ce5be9d"}, "method": 1, "data": {"date": 2019, "tag": "work", "content": "inserted successfully", "done": "false"}}]"""

        return strstrstrNew
    
    def findAll():
        
        cursor = colUsergao.find()

        dataJsonString = dumps(cursor)

        # dataList = loads(dataJsonString)
        
        return dataJsonString
    
    def findOne():
        
        one = colUsergao.aggregate( [
            {"$sample": { "size" : 1} },
        ] )
        
        oneD = dumps(one)
        
        return oneD
    
    def deleteOne(theContentToDel):
        
        # colUsergao.find_one_and_delete(filter, kwargs)
        
        strstrstrNew = """[{"_id": {"$oid": "6268c6faf4c2fd742ce5be9d"}, "method": 1, "data": {"date": 2019, "tag": "work", "content": "deleted successfully", "done": "false"}}]"""

        return strstrstrNew
    
   
    
    if method == 'inputContent':
        returnMessage = addOne(content)
    
    if method == 'retrieveAllContent':    
        returnMessage = findAll()
    
    if method == 'retrieveOneContent':    
        returnMessage = findOne()
    
    if method == 'deleteOneContent':    
        returnMessage = deleteOne(content)
        

    client.close()
    
    return returnMessage
    
    
    
    
    # =============================================================================
    
    
    
    
    
    # print("→" + "\n" + "arrpw")
    
    
    
    
    
    
    
    
    
    
                                                        













