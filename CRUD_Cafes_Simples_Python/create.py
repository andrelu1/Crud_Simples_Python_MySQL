# -*- encoding: utf-8 -*-

import mysql.connector
import datetime

connection = mysql.connector.connect(
  host="localhost",
  user="root",
  password="toor",
  database="cafes"
)

cursor = connection.cursor()

sql = "INSERT INTO cafes (nome, tipo, valor, created) VALUES (%s, %s, %s, %s)"
data = (
  'Café 01',
  'Arabia',
  'Valor',
  datetime.datetime.today()
)

cursor.execute(sql, data)
connection.commit()

cafeid = cursor.lastrowid

cursor.close()
connection.close()

print("Foi cadastrado um novo café:", cafeid)
