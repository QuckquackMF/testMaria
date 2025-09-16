# Start from a minimal Debian base image
FROM debian:bullseye-slim

# Install system dependencies and tools
RUN apt-get update && apt-get install -y \
    sudo \
    curl \
    gnupg \
    procps \
    locales \
    && rm -rf /var/lib/apt/lists/*

# Set up a locale to prevent errors with certain tools
RUN echo "en_US.UTF-8 UTF-8" > /etc/locale.gen && locale-gen

# Install Node.js (and npm)
RUN curl -fsSL https://deb.nodesource.com/setup_18.x | sudo bash - \
    && sudo apt-get update && sudo apt-get install -y nodejs \
    && sudo rm -rf /var/lib/apt/lists/*

# Install MariaDB server and client, and the globalization library
RUN sudo apt-get update && sudo apt-get install -y \
    mariadb-server \
    mariadb-client \
    libicu-dev \
    && sudo rm -rf /var/lib/apt/lists/*

# Install Python 3 and the Python debugger (debugpy)
RUN sudo apt-get update && sudo apt-get install -y python3 python3-pip \
    && sudo pip3 install debugpy \
    && sudo rm -rf /var/lib/apt/lists/*

# Create a non-root user for development to follow best practices
ARG USERNAME=vscode
ARG USER_UID=1000
ARG USER_GID=$USER_UID
RUN groupadd --gid $USER_GID $USERNAME \
    && useradd -s /bin/bash --uid $USER_UID --gid $USER_GID -m $USERNAME \
    && sudo usermod -aG sudo $USERNAME \
    && echo $USERNAME ALL=(ALL) NOPASSWD:ALL > /etc/sudoers.d/$USERNAME \
    && sudo chmod 0440 /etc/sudoers.d/$USERNAME

# Expose the MariaDB port
EXPOSE 3306

# Start MariaDB service and keep the container running
CMD ["sudo", "service", "mariadb", "start", "&&", "sleep", "infinity"]
