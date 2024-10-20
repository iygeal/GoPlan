#!/usr/bin/env python3
"""This module is used to set up the database
for the GoPlan web application, using environment variables
inside .env file.
"""


import mysql.connector
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Get the credentials from .env
db_user = os.getenv('GO_PLAN_USER')
db_password = os.getenv('GO_PLAN_MYSQL_PWD')
db_name = os.getenv('GO_PLAN_MYSQL_DB')
db_host = os.getenv('GO_PLAN_MYSQL_HOST')

# Connect to MySQL as root (or another admin user)
connection = mysql.connector.connect(
    host=db_host,
    user='root',  # Use root or an existing admin user
    # You'll need to put root's password in .env too
    password=os.getenv('ROOT_MYSQL_PWD')
)

cursor = connection.cursor()

# Create the database if it doesn't exist
cursor.execute(f"CREATE DATABASE IF NOT EXISTS {db_name};")

# Create the user if it doesn't exist
cursor.execute(
    f"CREATE USER IF NOT EXISTS '{db_user}'@'{db_host}' IDENTIFIED BY '{db_password}';")

# Grant privileges to the user on the database
cursor.execute(
    f"GRANT ALL PRIVILEGES ON {db_name}.* TO '{db_user}'@'{db_host}';")

# Flush privileges to make sure changes take effect
cursor.execute("FLUSH PRIVILEGES;")

# Commit and close connection
connection.commit()
cursor.close()
connection.close()

print("Database and user setup complete.")
