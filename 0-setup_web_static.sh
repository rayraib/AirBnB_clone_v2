#!/usr/bin/env bash
# script that sets up your web servers for the deployment of web_static
code="\\tlocation /hbnb_static/ {\n\talias /data/web_static/current;\n\t}"
sudo apt-get update -y
sudo apt-get install nginx -y
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/
sudo touch /data/web_static/releases/test/index.html
echo "test index" > /data/web_static/releases/test/index.html
sudo touch /data/web_static/current
sudo ln -sf /data/web_static/current /data/web_static/releases/test/
sudo chown -R ubuntu:ubuntu /data/
sudo sed -i "28i $code" /etc/nginx/sites-available/default
