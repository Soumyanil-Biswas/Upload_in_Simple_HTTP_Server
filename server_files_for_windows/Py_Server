#!/usr/bin/python3

from flask import Flask 
from flask_autoindex import AutoIndex
import os

app = Flask(__name__)

pwd = os.getcwd()
nav_path = pwd 

AutoIndex(app, browse_root=nav_path)    

if __name__ == "__main__":
    app.debug = True
    app.run(host= '0.0.0.0')
