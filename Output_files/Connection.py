import mysql.connector
    
mydb = mysql.connector.connect(
host='127.0.0.1',
user='root',
password=''
)
mycursor = mydb.cursor()


def GetConnection():
    return mycursor
