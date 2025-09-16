#!/bin/bash
set -e

# Ensure runtime directory exists with correct permissions
mkdir -p /run/mysqld
chown mysql:mysql /run/mysqld

# Initialize DB if not already initialized
if [ ! -d "/var/lib/mysql/mysql" ]; then
    echo "Initializing MariaDB data directory..."
    mysqld --initialize-insecure --user=mysql
    echo "MariaDB initialized."
fi

# Start the MariaDB server in foreground
exec mysqld
