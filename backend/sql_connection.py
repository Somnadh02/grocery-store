import datetime
import mysql.connector

cnx = None

def get_sql_connection():
  print("Opening mysql connection")
  global cnx

  if cnx is None:
    cnx = mysql.connector.connect(host='localhost',user='root', password='Data@321', database='grocery_store')

  return cnx