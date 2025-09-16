# Start from a Node.js image that also includes Python
FROM node:18-bullseye-slim

# Install MariaDB server, client, and Python debugger
# The Node.js image is based on Debian, so we can use apt-get
RUN apt-get update && apt-get -y install mariadb-server mariadb-client libicu-dev \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# Install the Python debugger
RUN pip install debugpy

# Run MariaDB on container start
CMD ["sudo", "service", "mariadb", "start"]
