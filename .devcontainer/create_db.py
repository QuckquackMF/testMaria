import mysql.connector

# Connect to MariaDB
conn = mysql.connector.connect(
    host="db",
    user="root",
    password="root"
)

cursor = conn.cursor()
cursor.execute("CREATE DATABASE IF NOT EXISTS mydatabase")
print("✅ Database 'mydatabase' created or already exists.")

cursor.close()
conn.close()
