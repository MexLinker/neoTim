# -*- coding: utf-8 -*-
"""
Created on Sat Dec 31 19:42:53 2022

@author: 26440
"""

from flask import Flask

from markupsafe import escape

from flask import request

import connect


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
    
# CORE
# timRecieve 
@app.route('/timRecieve', methods=['POST', 'GET'])
def timRecieve():
    if request.method == 'POST':
        print("req method is POST ")
        
        print(request.form['timMethod'])
        print(request.form['content'])
        
        timMethod = request.form['timMethod']
        
        contentToReturn = connect.connectFunc(timMethod, 1)
        
        print(contentToReturn)
        
        return contentToReturn
    
    
    
    if request.method == 'GET':
        
        timMethod = request.args['timMethod']
        
        contentToReturn = connect.connectFunc(timMethod, 1)
        
        return  contentToReturn
     














































# AA