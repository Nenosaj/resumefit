# Use the official PHP 8.3 FPM image
FROM php:8.3-fpm-alpine

# Set working directory
WORKDIR /var/www/html

# Install system dependencies
RUN apk add --no-cache \
    git \
    curl \
    libpq-dev \
    nginx \
    # For pdo_pgsql
    postgresql-dev

# Install PHP extensions
RUN docker-php-ext-install \
    pdo_pgsql \
    opcache

# Install Composer
COPY --from=composer:latest /usr/bin/composer /usr/local/bin/composer

# Expose port 9000 for FPM
EXPOSE 9000

# Start PHP-FPM
CMD ["php-fpm"]