FROM mcr.microsoft.com/devcontainers/universal:2

# Install MariaDB server and client and fix the libicu dependency
RUN apt-get update && apt-get -y install mariadb-server mariadb-client libicu-dev \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# The Universal image is already configured to run as a non-root user.
# You don't need to create one.

# Start MariaDB service and keep container running
CMD ["sudo", "service", "mariadb", "start", "&&", "sleep", "infinity"]
