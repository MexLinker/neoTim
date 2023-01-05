# # -*- coding: utf-8 -*-
# """
# Created on Sun Jan  1 09:19:33 2023

# @author: 26440
# """

import requests

# # =============================================================================
# # those are useful codes to access the server 
# # 
# # yourUserName = 'Mexlink'
# # 
# # postRespon = requests.post("http://127.0.0.1:5000/login", data={'username':yourUserName})
# # 
# # print(postRespon.text)
# # =============================================================================

helloTimeToPrint = ''''welcome to tim, type h for help\n, 
input 1 to add a verse to database \n
input 2 to retrieve all records\n
input 3 to retrieve random one of records\n
input 4 to delete one using matching content\n
\n'''

print(helloTimeToPrint)

inputContent = input()

if inputContent == 'h':
    print("this is the help for tim")
    
# what i will sent to server is {'method':1,'content':'this is content'}

if inputContent == '1':
    theItemToAdd = input("please input the item to add /n")
    postRespon = requests.post("http://127.0.0.1:5000/timRecieve", data={'timMethod':'inputContent','content':'ThisIsTheContent'})

if inputContent == '2':
    print("this is a test for retrive all")
    postRespon = requests.post("http://127.0.0.1:5000/timRecieve", data={'timMethod':'retrieveAllContent','content':'thisIsUseLessContentForRetrevingAll'})

if inputContent == '3':
    print("this is a test for retrive one")
    postRespon = requests.post("http://127.0.0.1:5000/timRecieve", data={'timMethod':'retrieveOneContent','content':'thisIsUseLessContentForRetrevingOne'})

if inputContent == '4':
    postRespon = requests.post("http://127.0.0.1:5000/timRecieve", data={'timMethod':'deleteOneContent','content':'thisIsDeleOneContentIWillAdd'})

# # m = 3
# # n = 7

print(postRespon.text)


# # def timHelp():
# #     print("this is the help for tim")
# #     return n+m
# # def addDatabase():
# #     theItemToAdd = input("please input the item to add")
# #     return n-m
# # def prod():
# #     return n*m
# # def div():
# #     return m/n
# # def rem():
# #     return m%n

# # def operations(op):
# #     switch={
# #        'h': timHelp(),
# #        '1': addDatabase(),
# #        '*': prod(),
# #        '/': div(),
# #        '%': rem(),
# #        }
# #     return switch.get(op,'Choose one of the following operator:+,-,*,/,%')

# # # opCode = input("chosee a operation from + - .. ==>")

# # ans = operations(inputContent)




# postRespon = requests.post("http://127.0.0.1:5000/timRecieve", data={'timMethod':'retrieveContent','content':'thisIsUseLessContentForRetreving'})

