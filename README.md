🚀 Deployment of Flask Web Application on AWS EC2
📌 Project Overview

This project demonstrates how to deploy a Flask-based web application on an AWS EC2 Ubuntu server.
The application is configured with:

Flask (Backend)

MySQL (Database)

Nginx (Reverse Proxy)

AWS EC2 (Cloud Server)

Git (Version Control)

The application is publicly accessible via EC2 public IP.

🏗 System Architecture
User (Browser)
      ↓
EC2 Public IP
      ↓
Nginx (Port 80)
      ↓
Flask Application (Port 5000)
      ↓
MySQL Database (Port 3306 - Internal)
🛠 Step-by-Step Deployment Guide
🔹 STEP 1 – Launch EC2 Instance

Go to AWS Console

Launch EC2 instance

Select:

AMI: Ubuntu

Instance Type: t2.micro or t3.micro

Create Key Pair (.pem file)

Configure Security Group:

Port 22 → SSH

Port 80 → HTTP

Port 5000 → (For testing)

Launch the instance.

🔹 STEP 2 – Connect to EC2 via SSH
chmod 400 key.pem
ssh -i key.pem ubuntu@your-public-ip
🔹 STEP 3 – Update System
sudo apt update -y
sudo apt upgrade -y
🔹 STEP 4 – Install Required Packages
sudo apt install python3-pip -y
sudo apt install python3-venv -y
sudo apt install git -y
sudo apt install nginx -y
sudo apt install mysql-server -y

Check services:

sudo systemctl status nginx
sudo systemctl status mysql
🔹 STEP 5 – Setup MySQL Database

Login to MySQL:

sudo mysql

Inside MySQL:

CREATE DATABASE flaskdb;

CREATE USER 'flaskuser'@'localhost' IDENTIFIED BY 'Flask@123';

GRANT ALL PRIVILEGES ON flaskdb.* TO 'flaskuser'@'localhost';

FLUSH PRIVILEGES;

EXIT;
🔹 STEP 6 – Create Users Table
mysql -u flaskuser -p

Enter password.

USE flaskdb;

CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    fullname VARCHAR(100),
    email VARCHAR(100),
    phone VARCHAR(15),
    username VARCHAR(50),
    password VARCHAR(255),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

SHOW TABLES;

EXIT;
🔹 STEP 7 – Clone Project from GitHub
git clone https://github.com/your-username/your-repository.git
cd your-repository
🔹 STEP 8 – Setup Virtual Environment
python3 -m venv venv
source venv/bin/activate

Install dependencies:

pip install flask
pip install mysql-connector-python
🔹 STEP 9 – Configure Database in app.py

Ensure database connection function:

def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="flaskuser",
        password="Flask@123",
        database="flaskdb"
    )
🔹 STEP 10 – Run Flask Application (Testing)

Make sure app runs on:

app.run(host="0.0.0.0", port=5000)

Run:

python app.py

Test in browser:

http://public-ip:5000
🔹 STEP 11 – Configure Nginx Reverse Proxy

Create config file:

sudo nano /etc/nginx/sites-available/flaskapp

Add:

server {
    listen 80;
    server_name your_public_ip;

    location / {
        proxy_pass http://127.0.0.1:5000;
        include proxy_params;
    }
}

Save and exit.

🔹 STEP 12 – Enable Nginx Configuration
sudo ln -s /etc/nginx/sites-available/flaskapp /etc/nginx/sites-enabled/

Test configuration:

sudo nginx -t

Restart Nginx:

sudo systemctl restart nginx
🔹 STEP 13 – Final Testing

Open browser:

http://your-public-ip
