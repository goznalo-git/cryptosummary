# Import necessary modules
import mysql.connector
import requests


# Obtain database credentials
with open("credentials.txt", "r") as f:
    creds = f.read().splitlines()


def query_database(database, query):
    """ Query the database and print the results """
    mycursor = database.cursor()
    mycursor.execute(query)

    cols = mycursor.column_names
    fulldict = {}

    while 1:
        row = mycursor.fetchone()

        # Exit the loop if None
        if not row:
            break

        fulldict[row[1]] = dict(zip(cols[2:], row[2:]))

    print(fulldict.keys())


# Database connection
mydb = mysql.connector.connect(
    host=creds[0],
    user=creds[1],
    password=creds[2],
    database=creds[3]
)

query = "SELECT * FROM my_money;"
query_database(mydb, query)


exit()


def get_crypto_price(crypto=""):
    """ Get the current crypto exchange rate, using eur.rate.sx """

    URL = "https://eur.rate.sx/" + crypto
    response = requests.get(URL)

    return response


response = get_crypto_price(btc)
print(response.text)
