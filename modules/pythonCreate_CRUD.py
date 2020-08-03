import os

python = ""
def CreateMaker(tableName,parameters):
    global python
    parameters1 = ""
    interrogant = ""

    for a in parameters:
        if parameters.index(a) == 0:
            parameters1+=a
            interrogant+='?'
        else:
            parameters1+=", "+a
            interrogant+=',?'
    python = ('''
from flask import Flask, escape, request
import Connection
import mysql.connector


app = Flask(__name__)

@app.route('/Insert')
def hello():
    name = request.args.get("name", "World")
    return f'Hello, {escape(name)}!'





''')
        

def Run(tableName,parameters):
    pCreate = './Output_files/Create'+tableName+'.py'
    if os.path.exists(pCreate):
        os.remove(pCreate)
        print ("Removed last file")
    CreateMaker(tableName,parameters);
    f = open(pCreate, "a")
    f.write(python)
    f.close()
    print("New file created")
    print()
