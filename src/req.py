# # -*- coding: utf-8 -*-
# """
# Created on Sun Jan  1 09:19:33 2023

# @author: 26440
# """

from sys import exit
import requests
from bson.json_util import dumps
from bson.json_util import loads



# # =============================================================================
# # those are useful codes to access the server 
# # 
# # yourUserName = 'Mexlink'
# # 
# # postRespon = requests.post("http://127.0.0.1:5000/login", data={'username':yourUserName})
# # 
# # print(postRespon.text)
# # =============================================================================

helloTimeToPrint = '''Welcome to tim,\nYour neoTim\nType h for help'''

print(helloTimeToPrint)

inputContent = input()

if inputContent == 'h':
    helpContent = '''
    input 1 to add a verse to database \n
    input 2 to retrieve all records\n
    input 3 to retrieve random one of records\n
    input 4 to delete one using matching content\n'''
    
    print("this is the help for tim")
    print(helpContent)
    
    exit()
    
# what i will sent to server is {'method':1,'content':'this is content'}


URLofService = "http://127.0.0.1:3002"


if inputContent == '1':
    theItemToAdd = input("please input the item to add \n")
    postRespon = requests.post( URLofService +  "/timRecieve", data={'timMethod':'inputContent','content':theItemToAdd})

if inputContent == '2':
    print("this is a test for retrive all")
    postRespon = requests.post( URLofService + "/timRecieve", data={'timMethod':'retrieveAllContent','content':'thisIsUseLessContentForRetrevingAll'})

if inputContent == '3':
    print("this is a test for retrive one")
    postRespon = requests.post( URLofService + "/timRecieve", data={'timMethod':'retrieveOneContent','content':'thisIsUseLessContentForRetrevingOne'})

if inputContent == '4':
    theItemToDel = input("input the item to delete\n")
    postRespon = requests.post( URLofService + "/timRecieve", data={'timMethod':'deleteOneContent','content':theItemToDel})

# # m = 3
# # n = 7


# print(postRespon.text)

# print(loads(postRespon))

# postString = dumps(postRespon)

# postList = loads(postString)

# for item in postList:
#     print( item )


dataList = loads(postRespon.text)

for item in dataList:
        print("  ➙  " + item["data"]["content"]  +  "\n")
        # print("K")










