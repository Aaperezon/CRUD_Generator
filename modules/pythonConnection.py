import os
import mysql.connector

python = ""
def ConnectionMaker(servername, username, password):
    global python
    python = (
'''import mysql.connector
    
mydb = mysql.connector.connect(
host=\''''+servername+'''\',
user=\''''+username+'''\',
password=\''''+password+'''\'
)
mycursor = mydb.cursor()


def GetConnection():
    return mycursor
'''
)


def Run(servername, username, password):
    pConnection = './Output_files/Connection.py'
    if (os.path.exists(pConnection)):
        os.remove(pConnection)
        print ("Removed last file")
    ConnectionMaker(servername, username, password);
    f = open(pConnection, "a")
    f.write(python)
    f.close()
    print("New file created")
