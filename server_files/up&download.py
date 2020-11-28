#!/usr/bin/python3

'''
Both Upload and Download file
'''

from flask import Flask, render_template, request
from werkzeug.utils import secure_filename

from flask_autoindex import AutoIndex
import os

app = Flask(__name__)

@app.route('/upload')
def upload1_file():
    return render_template('code.html')
	
@app.route('/uploader', methods = ['GET', 'POST'])
def upload2_file():
    if request.method == 'POST':
        f = request.files['file']
        f.save(secure_filename(f.filename))
        return 'file uploaded successfully'

cwd = os.getcwd()
nav_path = cwd # update your own parent directory here

obj = Flask(__name__)
AutoIndex(obj, browse_root=nav_path)    

if __name__ == "__main__":
    obj.debug = True
    obj.run(host= '0.0.0.0')