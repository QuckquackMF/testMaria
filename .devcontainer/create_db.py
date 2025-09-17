import mysql.connector

# Establish the connection
mydb = mysql.connector.connect(
  host="localhost", 
  user="root",     
  password=""     
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE IF NOT EXISTS mydatabase")
