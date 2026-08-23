# -*- coding: utf-8 -*-
"""
Created on Sun Jan  1 09:19:33 2023

@author: 26440
"""

from sys import exit
import requests
from bson.json_util import loads
import hashlib
import random
import json

# =================
# TRANSLATE - YOUDAO
# =================

def generate_sign(app_id, query, salt, app_secret):
    sign_str = app_id + query + str(salt) + app_secret
    return hashlib.md5(sign_str.encode('utf-8')).hexdigest()


def youdao_translate(query):
    if not isinstance(query, str):
        print("Error: query is not a string. It is:", type(query), query)
        return "Invalid input"

    if all(ord(char) < 128 for char in query):
        return query

    app_id = "5da7b542e6b08ef9"
    app_secret = "OlJoYZRAbdfYUDDkAFXs52CeKdGpr1LT"
    url = "https://openapi.youdao.com/api"
    salt = random.randint(1, 65536)
    sign = generate_sign(app_id, query, salt, app_secret)

    params = {
        "q": query,
        "from": "zh-CHS",
        "to": "en",
        "appid": app_id,   # Fixed: was wrong "appKey"
        "salt": salt,
        "sign": sign,
    }

    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        result = response.json()

        if result.get("errorCode") != "0":
            return f"Translation failed, code:{result.get('errorCode')}"

        if 'translation' in result:
            return result['translation'][0]
        else:
            return "Translation result empty: " + json.dumps(result, ensure_ascii=False)
    except Exception as e:
        return f"Translate network error: {str(e)}"


# =================
# MAIN CLIENT LOGIC
# =================

helloTimeToPrint = '''Welcome to tim,
Your neoTim
Type h for help'''

print(helloTimeToPrint)
inputContent = input()

if inputContent == 'h':
    helpContent = '''
    input 1 to add a verse to database \n
    input 2 to retrieve all records\n
    input 3 to retrieve random one of records\n
    input 4 to delete one using matching content\n
    input 5 to retrive a translated content\n'''

    print("this is the help for tim")
    print(helpContent)
    exit()


URLofService = "http://127.0.0.1:5000"
postRespon = None

try:
    if inputContent == '1':
        theItemToAdd = input("please input the item to add \n")
        postRespon = requests.post(
            URLofService + "/timRecieve",
            data={'timMethod': 'inputContent', 'content': theItemToAdd},
            timeout=10
        )
        postRespon.raise_for_status()
        print("Add operation result: ", postRespon.text)
        exit()   # Important: do NOT fall‑through to retrieve‑print code

    if inputContent == '2':
        print("this is a test for retrive all")
        postRespon = requests.post(
            URLofService + "/timRecieve",
            data={'timMethod': 'retrieveAllContent', 'content': 'thisIsUseLessContentForRetrevingAll'},
            timeout=10
        )

    if inputContent == '3':
        print("this is a test for retrive one")
        postRespon = requests.post(
            URLofService + "/timRecieve",
            data={'timMethod': 'retrieveOneContent', 'content': 'thisIsUseLessContentForRetrevingOne'},
            timeout=10
        )

    if inputContent == '4':
        theItemToDel = input("input the item to delete\n")
        postRespon = requests.post(
            URLofService + "/timRecieve",
            data={'timMethod': 'deleteOneContent', 'content': theItemToDel},
            timeout=10
        )
        postRespon.raise_for_status()
        print("Delete operation result: ", postRespon.text)
        exit()  # Important: stop here after delete

    if inputContent == '5':
        print("retrive one with translate")
        postRespon = requests.post(
            URLofService + "/timRecieve",
            data={'timMethod': 'retrieveOneContent', 'content': 'thisIsUseLessContentForRetrevingOne'},
            timeout=10
        )
        postRespon.raise_for_status()
        dataList = loads(postRespon.text)
        for item in dataList:
            if isinstance(item, dict) and "data" in item and "content" in item["data"]:
                text = item["data"]["content"]
                trans_text = youdao_translate(text)
                print(f"Original: {text}")
                print(f"English: {trans_text}\n")
            else:
                print(f"Unexpected record format: {item}")
        exit()

    # For read‑only actions: 2, 3
    postRespon.raise_for_status()
    dataList = loads(postRespon.text)

    for item in dataList:
        # Safe guard before dict access
        if isinstance(item, dict) and "data" in item and "content" in item["data"]:
            print("  ➙  " + item["data"]["content"] + "\n")
        else:
            print(f"Warning, unexpected item: {item}")

except requests.exceptions.RequestException as req_err:
    print(f"Network / HTTP error: {req_err}")
    exit()
except Exception as general_err:
    print(f"Runtime error: {general_err}")
    exit()


