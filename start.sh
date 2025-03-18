#!/bin/bash

# Set default PORT if not provided by environment
export PORT=${PORT:-8080}

# Replace ${PORT} placeholder in nginx.conf with actual PORT from environment
sed -i "s/\${PORT}/$PORT/g" /etc/nginx/nginx.conf

# Create required directories if they don't exist
mkdir -p /var/log/nginx
touch /var/log/nginx/error.log /var/log/nginx/access.log
chown -R www-data:www-data /var/log/nginx

# Check if nginx.conf is valid
echo "Checking Nginx configuration..."
nginx -t

# Start supervisord to manage all services
exec /usr/bin/supervisord -c /etc/supervisor/conf.d/supervisord.conf