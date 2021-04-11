import mysql.connector
import requests

mydb = mysql.connector.connect(
    host="localhost",
    user="gonzalo",
    password="pass1234",
    database="cryptocoins"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM my_money;")

for line in mycursor:
    print(line)
