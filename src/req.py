# -*- coding: utf-8 -*-
"""
Created on Sun Jan  1 09:19:33 2023

@author: 26440
"""

import requests

# helloRespon = requests.get("http://127.0.0.1:5000/")

# print(respon.text)

# from flask import request as req2

# req2.get("http://www.baidu.com")

# req2.accept_charset

postRespon = requests.post("http://127.0.0.1:5000/login", data={'username':'valueKKKKKKKKKKKKKK'})

print(postRespon.text)





