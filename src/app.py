# -*- coding: utf-8 -*-
"""
Created on Sat Dec 31 19:42:53 2022

@author: 26440
"""

from flask import Flask

from markupsafe import escape

from flask import request


app = Flask(__name__)

@app.route("/<name>")
def helloExp(name):
    return f"Hello, {escape(name)}!"

@app.route('/')
def index():
    return 'Index Page， <a href="hello">this will link you to {/hello} dir</a>'

@app.route('/hello')
def hello():
    return 'Hello, World'

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return f'Post {post_id}'

    # eg:http://127.0.0.1:5000/post/1234
    # it will show Post 1234
    
@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    # show the subpath after /path/
    return f'Subpath {escape(subpath)}'
    # http://127.0.0.1:5000/path/you/know/there/will/be/more/path
    
@app.route('/login', methods=['POST', 'GET'])
def login():
    # error = None
    if request.method == 'GET':
        print("falls in first if")
        print(request.form['username'])
    if request.method == 'POST':
        print("falls in second if")
        print("most likely to be POST ")
        print(request.form['username'])
    else:
        print("it is neither GET or POST")
    return 'login.html'















































# AA