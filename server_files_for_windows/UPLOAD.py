#!/usr/bin/python3

import os
from flask import Flask, flash, request, redirect, url_for, send_from_directory
from werkzeug.utils import secure_filename

from flask_autoindex import AutoIndex

#Present Working directory of server
pwd = os.getcwd()
nav_path = pwd

#Creating Custom Directory
directory = "UPLOADED_FOLDER"

#Destination path to store Uploaded File
UPLOAD_FOLDER = nav_path+'/'+directory

#mode/permission of directory created

#mode = 0o777             #Change directory permission acc. to will

#Creating Directory
#os.mkdir(UPLOAD_FOLDER, mode)


#Upload File Extensions Validation
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'py', 'c', 'html'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
'''
#Server pwd
server_pwd = AutoIndex(app, browse_root=nav_path)
'''
#Checking Validity of Extension wrt Alloted set ALLOWED_EXTENSIONS
def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.',1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # Check if the post request has the file part
        if 'file' not in request.files:
            flash('No selected file')
            return redirect(request.url)
        file = request.files['file']
        #If user does not select file, browser also
        #submit an empty part without filename
        if file.name == '':
            flash('No selected file')
            return redirect(request.url)
        
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))
            return redirect(url_for('uploaded_file', filename=filename))
    
    return '''
    <!DOCTYPE html>
    
    <html lang="en"> 
    <body style="background-color:#93B874;">

        <h1><u><strong><em>Upload/Download your preferred Files/Folders:</em></strong></u></h1>
        <h5>By Soumyanil Biswas</h5>
   <h6>Connect with me: <a href="https://www.linkedin.com/in/soumyanil-biswas-4b7603195/">LinkedIn</a></h6>
&nbsp; 
   <figure>
      <img src="https://www.groovypost.com/wp-content/uploads/2018/05/Nearby_Sharing_Files_Wireless_Featured-1000x450.jpg" alt="photo">
   
   <p>This Picture is taken from <a href="https://www.groovypost.com/">source</a> </p>
&nbsp;
   </figure>
        <form method=post enctype=multipart/form-data>
            <p>Upload File: <input type=file name=file>
            <input type=submit value=Upload></p>
        </form>
        <form>
            <p>Copy File: <input type=file name=server_pwd>
            <input type=submit ></p> 
        </form>
    '''

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)
'''
@app.route('/downloads/')
def downloaded_file():
''' 

if __name__ == "__main__":
    app.debug = True
    app.run(host= '0.0.0.0')