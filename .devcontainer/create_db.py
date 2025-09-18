import mysql.connector
import time

host = "127.0.0.1"  # Use TCP
user = "root"
password = ""  # Change if you set a root password
database = "mydatabase"

print("⏳ Waiting for MariaDB to be ready... (retrying every 30 seconds)")

while True:
    try:
        conn = mysql.connector.connect(
            host=host,
            user=user,
            password=password
        )
        print("✅ Connected to MariaDB!")
        break
    except mysql.connector.Error as e:
        print(f"Waiting for database... ({e})")
        time.sleep(30)  # wait 30 seconds before retrying

cursor = conn.cursor()
cursor.execute(f"CREATE DATABASE IF NOT EXISTS {database}")
print(f"✅ Database '{database}' created or already exists.")
cursor.close()
conn.close()
