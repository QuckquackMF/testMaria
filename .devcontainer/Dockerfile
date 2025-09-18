# Base image
FROM debian:bullseye-slim

# Install dependencies
RUN apt-get update && apt-get install -y \
    sudo \
    curl \
    gnupg \
    procps \
    locales \
    mariadb-server \
    mariadb-client \
    libicu-dev \
    python3 \
    python3-pip \
    nodejs \
    netcat \
    && rm -rf /var/lib/apt/lists/*

# Generate locale
RUN echo "en_US.UTF-8 UTF-8" > /etc/locale.gen && locale-gen

# Install Python MySQL connector
RUN pip3 install mysql-connector-python

# Create non-root vscode user
ARG USERNAME=vscode
ARG USER_UID=1000
ARG USER_GID=$USER_UID
RUN groupadd --gid $USER_GID $USERNAME \
  && useradd -m -s /bin/bash --uid $USER_UID --gid $USER_GID $USERNAME \
  && echo "$USERNAME ALL=(ALL) NOPASSWD:ALL" > /etc/sudoers.d/$USERNAME \
  && chmod 0440 /etc/sudoers.d/$USERNAME

# Set up MariaDB runtime folder
RUN mkdir -p /run/mysqld && chown -R mysql:mysql /run/mysqld

# Expose MariaDB port
EXPOSE 3306

# Copy Python script and requirements
COPY create_db.py /create_db.py
COPY requirements.txt /requirements.txt
RUN pip3 install -r /requirements.txt

# Initialize MariaDB and create database on container start
CMD mysqld_safe --datadir=/var/lib/mysql & \
    echo "Waiting for MariaDB to start..." && \
    for i in {1..30}; do nc -z localhost 3306 && break || sleep 1; done && \
    python3 /create_db.py && \
    tail -f /dev/null
