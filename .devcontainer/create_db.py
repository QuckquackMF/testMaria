import mysql.connector
import time

# Wait a few seconds to let MariaDB start
time.sleep(5)

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password=""
)

cursor = conn.cursor()
cursor.execute("CREATE DATABASE IF NOT EXISTS mydatabase")
print("✅ Database 'mydatabase' created or already exists.")

cursor.close()
conn.close()
