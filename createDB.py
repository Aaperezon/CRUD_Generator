import mysql.connector
import json
from modules import phpConnection,phpCreate_CRUD,phpRead_CRUD
from modules import pythonConnection,pythonCreate_CRUD,pythonRead_CRUD

with open('config.json') as json_config:
	json_config = json.load(json_config)

mydb = mysql.connector.connect(
  host=json_config['host'],
  user=json_config['user'],
  password=json_config['password']
)
mycursor = mydb.cursor()

mycursor.execute("DROP DATABASE IF EXISTS "+json_config['nameDB'])
mycursor.execute("CREATE DATABASE "+json_config['nameDB'])
mycursor.execute("USE "+json_config['nameDB'])

"""
for query in open(p):
	mycursor.execute(query)
"""


pythonConnection.Run(json_config['host'],json_config['user'],json_config['password'])
pythonCreate_CRUD.Run('TablaDePrueba',['jeje int', 'jaja float not null'])

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
	print (stringToCreateTable)
	#print (dataName)
	mycursor.execute("CREATE TABLE "+tableName+" ("+ stringToCreateTable+" );")

	#phpCreate_CRUD.Run(tableName,dataName[2:])



print ()

"""
for numTable in range (len(json_config['tableInfo'])):
	nameTable = json_config['tableInfo'][numTable]['nameTable']
	column = json_config['tableInfo'][numTable]['column']
	dataName = []
	#dataType = []
	#condition = []
	listToCreateTable = []
	for i in range (0,len(column)):
		if (i % 3 == 0):
			dataName.append(column[i])
			#dataType.append(column[i+1])
			#condition.append(column[i+2])
			if (i!=0):
				listToCreateTable.append(", "+column[i]+" "+column[i+1]+" "+column[i+2])
			else:
				listToCreateTable.append(column[i]+" "+column[i+1]+" "+column[i+2])
    				
	stringToCreateTable = ' '.join([str(elem) for elem in listToCreateTable])
	mycursor.execute("CREATE TABLE "+nameTable+" ("+ stringToCreateTable+" );")

	phpCreate_CRUD.Run(nameTable,dataName[2:])
	phpRead_CRUD.Run(nameTable)

phpConnection.Run(json_config['host'],json_config['user'],json_config['password'],json_config['nameDB'])



"""
