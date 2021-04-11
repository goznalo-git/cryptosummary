# Import necessary modules
import mysql.connector
import requests


# Obtain database credentials
with open("credentials.txt", "r") as f:
    creds = f.read().splitlines()


def query_database(database, query):
    """ Query the database and returns the cursor and columns """
    mycursor = database.cursor()
    mycursor.execute(query)

    cols = mycursor.column_names

    return cols, mycursor


def get_portfolio(cols, cursor):
    """
    Take the column names and the cursor, output a dictionary of
    dictionaries, each containing a crypto -> tokens assignment
    """
    portfolio = {}

    while 1:
        row = cursor.fetchone()

        # Exit the loop if None
        if not row:
            break

        values = map(float, row[2:])
        portfolio[row[1]] = dict(zip(cols[2:], values))

    return portfolio


# Database connection
mydb = mysql.connector.connect(
    host=creds[0],
    user=creds[1],
    password=creds[2],
    database=creds[3]
)

query = "SELECT * FROM my_money;"

portfolio = get_portfolio(*query_database(mydb, query))

print(portfolio["Coinbase"])

exit()


def get_crypto_price(crypto=""):
    """ Get the current crypto exchange rate, using eur.rate.sx """

    URL = "https://eur.rate.sx/" + crypto
    response = requests.get(URL)

    return response


response = get_crypto_price(btc)
print(response.text)
