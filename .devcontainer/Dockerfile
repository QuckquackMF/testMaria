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

# Install Python requirements
COPY requirements.txt /tmp/
RUN pip3 install -r /tmp/requirements.txt

# Initialize MariaDB data directory
RUN mysqld --initialize-insecure --user=mysql --datadir=/var/lib/mysql

# Create non-root vscode user
ARG USERNAME=vscode
ARG USER_UID=1000
ARG USER_GID=$USER_UID
RUN groupadd --gid $USER_GID $USERNAME \
  && useradd -m -s /bin/bash --uid $USER_UID --gid $USER_GID $USERNAME \
  && echo "$USERNAME ALL=(ALL) NOPASSWD:ALL" > /etc/sudoers.d/$USERNAME \
  && chmod 0440 /etc/sudoers.d/$USERNAME

# Expose MariaDB port
EXPOSE 3306

# Start MariaDB in foreground, keep container alive
CMD ["bash", "-c", "mkdir -p /run/mysqld && chown -R mysql:mysql /run/mysqld && exec mysqld --user=mysql --datadir=/var/lib/mysql"]
