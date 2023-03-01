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

sql = "UPDATE cafes SET nome = %s, tipo = %s, valor = %s, WHERE id = %s"
data = (
  'Café',
  'Arabia',
  'R$200',
  1
)

cursor.execute(sql, data)
connection.commit()

recordsaffected = cursor.rowcount

cursor.close()
connection.close()

print(recordsaffected, " registros alterados")
