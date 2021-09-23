#==================================================================
# This is a contribution from 'Ar-P Corp' development department. 
# Developer: Aarón Pérez Ontiveros								  
#
# Install modules for Python3.5+
#    pip install mysql.connector
#=================================================================
import mysql.connector
import json
from modules import phpConnection,phpCreate_CRUD,phpRead_CRUD,phpDelete_CRUD,phpUpdate_CRUD
#from modules import pythonConnection,pythonCreate_CRUD,pythonRead_CRUD

with open('config.json') as json_config:
	json_config = json.load(json_config)

mydb = mysql.connector.connect(
  host=json_config['host'],
  port=json_config['port'],
  user=json_config['user'],
  password=json_config['password']
)
mycursor = mydb.cursor()

mycursor.execute("DROP DATABASE IF EXISTS "+json_config['nameDB'])
mycursor.execute("CREATE DATABASE "+json_config['nameDB'])
mycursor.execute("USE "+json_config['nameDB'])

for i in range (0,len(json_config['tableInfo'])):
	tableName = json_config['tableInfo'][i]['nameTable']
	print (tableName)
	dataName = []
	stringToCreateTable = ""
	for j in range (0,len(json_config['tableInfo'][i]['atributes'])):
		atribute = json_config['tableInfo'][i]['atributes'][j]['atribute']
		dataName.append(atribute[0])
		aux = ' '.join([str(elem) for elem in atribute])
		if (j != 0):
			stringToCreateTable += (', '+aux)
		else:
			stringToCreateTable += aux
	#print (stringToCreateTable)
	#print (dataName)
	mycursor.execute("CREATE TABLE "+tableName+" ("+ stringToCreateTable+" );")

	phpCreate_CRUD.Run(tableName,dataName[2:])
	phpRead_CRUD.Run(tableName)
	phpDelete_CRUD.Run(tableName)
	phpUpdate_CRUD.Run(tableName)
phpConnection.Run(json_config['host'],json_config['user'],json_config['password'],json_config['nameDB'])