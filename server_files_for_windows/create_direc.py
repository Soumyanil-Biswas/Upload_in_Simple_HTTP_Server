#!/usr/bin/python3

import os

nav_path = 1
UPLOAD_FOLDER = 1

def crt_direc():

    global nav_path
    global UPLOAD_FOLDER

    #Present Working directory of server
    pwd = os.getcwd()
    nav_path = pwd

    #Creating Custom Directory
    directory = "UPLOADED_FOLDER"

    #Destination path to store Uploaded File
    UPLOAD_FOLDER = os.path.join(pwd, directory)

    #mode/permission of directory created

    mode = 0o777             #Change directory permission acc. to will

    #Creating Directory
    os.mkdir(UPLOAD_FOLDER, mode)

    return UPLOAD_FOLDER
    #print("Directory'%s' created" % directory)

crt_direc()
print(UPLOAD_FOLDER)
