import mysql.connector
import time

host = "127.0.0.1"
user = "root"
password = ""  # No password
database = "mydatabase"

print("⏳ Waiting for database to be ready...")

while True:
    try:
        conn = mysql.connector.connect(
            host=host,
            user=user,
            password=password
        )
        break
    except mysql.connector.Error:
        print("Waiting for database... retrying in 5 seconds")
        time.sleep(5)

cursor = conn.cursor()
cursor.execute(f"CREATE DATABASE IF NOT EXISTS {database}")
print(f"✅ Database '{database}' created or already exists.")

cursor.close()
conn.close()
