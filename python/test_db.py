import mysql.connector
from dotenv import load_dotenv
import os

# Load .env file
load_dotenv()

# Get variables from .env
db_host = os.getenv("DB_HOST")
db_user = os.getenv("DB_USER")
db_pass = os.getenv("DB_PASS")
db_name = os.getenv("DB_NAME")

print("DB_HOST:", db_host)  # debug print
print("DB_USER:", db_user)  # debug print

# Attempt connection
try:
    conn = mysql.connector.connect(
        host=db_host,
        user=db_user,
        password=db_pass,
        database=db_name
    )
    print("Connection successful!")
    conn.close()
except mysql.connector.Error as err:
    print("Connection failed:", err)