import mysql.connector
import requests

mydb = mysql.connector.connect(
    host="localhost",
    user="sample_user",
    password="sample_password",
    database="cryptocoins"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM my_money;")

for line in mycursor:
    print(line)
