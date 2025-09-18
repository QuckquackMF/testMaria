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
    netcat \
    && rm -rf /var/lib/apt/lists/*

# Generate locale
RUN echo "en_US.UTF-8 UTF-8" > /etc/locale.gen && locale-gen

# Create non-root vscode user
ARG USERNAME=vscode
ARG USER_UID=1000
ARG USER_GID=$USER_UID
RUN groupadd --gid $USER_GID $USERNAME \
  && useradd -m -s /bin/bash --uid $USER_UID --gid $USER_GID $USERNAME \
  && echo "$USERNAME ALL=(ALL) NOPASSWD:ALL" > /etc/sudoers.d/$USERNAME \
  && chmod 0440 /etc/sudoers.d/$USERNAME

# Copy Python script
COPY .devcontainer/create_db.py /workspace/.devcontainer/create_db.py

# Install Python connector
RUN pip3 install mysql-connector-python

# Expose MariaDB port
EXPOSE 3306

# Start MariaDB and keep container alive
CMD ["/bin/bash", "-c", "mkdir -p /run/mysqld && chown -R mysql:mysql /run/mysqld && mysqld_safe --datadir=/var/lib/mysql & sleep 5 && python3 /workspace/.devcontainer/create_db.py && tail -f /dev/null"]
