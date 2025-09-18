import mysql.connector
import time

host = "localhost"
user = "root"
password = ""
database = "mydatabase"

# Wait until MariaDB is ready
for _ in range(30):
    try:
        conn = mysql.connector.connect(
            host=host,
            user=user,
            password=password
        )
        break
    except mysql.connector.Error:
        print("Waiting for database...")
        time.sleep(2)
else:
    raise Exception("Database not ready after 30 attempts.")

cursor = conn.cursor()
cursor.execute(f"CREATE DATABASE IF NOT EXISTS {database}")
print(f"✅ Database '{database}' created or already exists.")

cursor.close()
conn.close()
