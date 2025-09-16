# Start from a minimal Debian base image
FROM debian:bullseye-slim

# Install system dependencies and tools
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

# Set up locale to prevent errors with some tools
RUN echo "en_US.UTF-8 UTF-8" > /etc/locale.gen && locale-gen

# Install debugpy for Python debugging
RUN pip3 install debugpy

# Create non-root vscode user
ARG USERNAME=vscode
ARG USER_UID=1000
ARG USER_GID=$USER_UID

RUN groupadd --gid $USER_GID $USERNAME \
  && useradd -m -s /bin/bash --uid $USER_UID --gid $USER_GID $USERNAME \
  && echo "$USERNAME ALL=(ALL) NOPASSWD:ALL" > /etc/sudoers.d/$USERNAME \
  && chmod 0440 /etc/sudoers.d/$USERNAME

# Copy entrypoint script and make executable
COPY docker-entrypoint.sh /usr/local/bin/docker-entrypoint.sh
RUN chmod +x /usr/local/bin/docker-entrypoint.sh

# Expose MariaDB port
EXPOSE 3306

# Use root to run entrypoint and start MariaDB
USER root
ENTRYPOINT ["/usr/local/bin/docker-entrypoint.sh"]

# Switch back to vscode user for normal terminal/shell usage
USER $USERNAME

# Default command to run MariaDB server
CMD ["mysqld"]
