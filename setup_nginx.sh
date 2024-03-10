#!/bin/sh

if [ "$ENV" = "dev" ]; then
  SERVER_NAME="dev.blockcerts.accredible.com"
elif [ "$ENV" = "production" ]; then
  SERVER_NAME="blockcerts.accredible.com"
else
  SERVER_NAME="127.0.0.1"
fi

sed -i "s/<server-name>/$SERVER_NAME/g" /etc/nginx/sites-available/cert_issuer
