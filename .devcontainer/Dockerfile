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
    && rm -rf /var/lib/apt/lists/*

# Generate locale
RUN echo "en_US.UTF-8 UTF-8" > /etc/locale.gen && locale-gen

# Initialize MariaDB database directory (important!)
RUN mysql_install_db --user=mysql --datadir=/var/lib/mysql

# Install mysql-connector for Python
RUN pip3 install mysql-connector-python

# Create vscode user
ARG USERNAME=vscode
ARG USER_UID=1000
ARG USER_GID=$USER_UID

RUN groupadd --gid $USER_GID $USERNAME \
  && useradd -m -s /bin/bash --uid $USER_UID --gid $USER_GID $USERNAME \
  && echo "$USERNAME ALL=(ALL) NOPASSWD:ALL" > /etc/sudoers.d/$USERNAME \
  && chmod 0440 /etc/sudoers.d/$USERNAME

# Expose MariaDB port
EXPOSE 3306

# Default command just keeps container alive
CMD ["sleep", "infinity"]
