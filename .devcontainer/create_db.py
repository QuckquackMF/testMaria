import mysql.connector
import time

socket_path = "/run/mysqld/mysqld.sock"
database_name = "mydatabase"

print(f"⏳ Waiting for MariaDB to be ready at {socket_path}...")

while True:
    try:
        conn = mysql.connector.connect(
            user="root",
            unix_socket=socket_path
        )
        break  # connection successful
    except mysql.connector.Error as e:
        print(f"Waiting for database... retrying in 5 seconds ({e})")
        time.sleep(5)

print("✅ Connected to MariaDB!")

cursor = conn.cursor()
cursor.execute(f"CREATE DATABASE IF NOT EXISTS {database_name}")
print(f"✅ Database '{database_name}' created or already exists.")

cursor.close()
conn.close()
