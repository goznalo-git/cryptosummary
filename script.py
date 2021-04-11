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


def query_database(query):

    mycursor = mydb.cursor()
    mycursor.execute(query)
    myresult = mycursor.fetchall()

    for line in myresult:
        print(line)


query = "SELECT * FROM my_money;"
query_database(query)


def get_latest_crypto_price(crypto=""):

    URL = "https://eur.rate.sx/" + crypto
    response = requests.get(URL)

    return response


response = get_latest_crypto_price()
print(response.text)
