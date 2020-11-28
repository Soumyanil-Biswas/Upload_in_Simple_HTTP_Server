#!/usr/bin/python3

from flask import Flask, render_template, request,  url_for, redirect
from werkzeug.utils import secure_filename

app = Flask(__name__)

@app.route('/')
def redirec():
    return render_template('code.html')
	
@app.route('/uploaded', methods = ['GET', 'POST'])
def upload2_file():
    if request.method == 'POST':
        f = request.files['file']  
        
        # ----> werkzeug.exceptions.BadRequestKeyError: 400 Bad Request: The browser (or proxy) sent a request that this server could not understand.
        # KeyError: 'file'

        f.save(secure_filename(f.filename))
        return 'file uploaded successfully'
		
if __name__ == '__main__':
   app.debug = True
   app.run(host= '0.0.0.0')
