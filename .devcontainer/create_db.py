import mysql.connector

# Connect with root user (password set to 'root' in Dockerfile)
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root"
)

mycursor = mydb.cursor()

# Create database if not exists
mycursor.execute("CREATE DATABASE IF NOT EXISTS mydatabase")

print("✅ Database 'mydatabase' created or already exists.")

mycursor.close()
mydb.close()
