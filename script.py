# Import necessary modules
import mysql.connector
import requests


# Obtain database credentials
with open("credentials.txt", "r") as f:
    creds = f.read().splitlines()

# Connect to MySQL using the module
mydb = mysql.connector.connect(
    host=creds[0],
    user=creds[1],
    password=creds[2],
    database=creds[3]
)

mycursor = mydb.cursor()

query = "SELECT * FROM my_money;"

mycursor.execute(query)

myresult = mycursor.fetchall()

for line in myresult:
    print(line)
