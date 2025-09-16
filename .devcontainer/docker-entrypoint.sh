#!/bin/bash
set -e

# Ensure runtime directory exists with correct ownership
mkdir -p /run/mysqld
chown mysql:mysql /run/mysqld

# Initialize database if not initialized yet
if [ ! -d "/var/lib/mysql/mysql" ]; then
  echo "Initializing MariaDB data directory..."
  mysqld --initialize-insecure --user=mysql
  echo "MariaDB data directory initialized."
fi

# Start MariaDB server in foreground (keeps container alive)
exec mysqld
