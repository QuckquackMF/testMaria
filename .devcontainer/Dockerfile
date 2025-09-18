# .devcontainer/Dockerfile
FROM ubuntu:22.04

# Install MariaDB, Python, and tools
RUN apt-get update && apt-get install -y \
    mariadb-server \
    python3 \
    python3-pip \
    locales \
    sudo \
    netcat \
    && rm -rf /var/lib/apt/lists/*

# Set locale
RUN echo "en_US.UTF-8 UTF-8" > /etc/locale.gen && locale-gen

# Install Python dependencies
COPY requirements.txt /requirements.txt
RUN pip3 install -r /requirements.txt

# Create vscode user
RUN groupadd --gid 1000 vscode \
    && useradd -m -s /bin/bash --uid 1000 --gid 1000 vscode \
    && echo "vscode ALL=(ALL) NOPASSWD:ALL" > /etc/sudoers.d/vscode \
    && chmod 0440 /etc/sudoers.d/vscode

# Prepare MariaDB runtime directory
RUN mkdir -p /run/mysqld && chown -R mysql:mysql /run/mysqld

# Copy your database creation script
COPY create_db.py /workspace/.devcontainer/create_db.py

# Switch to vscode user
USER vscode
WORKDIR /workspace
