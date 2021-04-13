# Import necessary modules
import mysql.connector
import requests

bold = '\033[1m'
end = '\033[0m'

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


try:
    # Database connection
    mydb = mysql.connector.connect(
        host=creds[0],
        user=creds[1],
        password=creds[2],
        database=creds[3]
    )

    query = "SELECT * FROM my_money;"
    portfolio = get_portfolio(*query_database(mydb, query))

except mysql.connector.errors.InterfaceError:
    print(bold + "MySQL connection Error" + end +
          ": MySQL is probably not running. Please start it, with\n\tsudo systemctl start mysql\nif you are running a modern Linux system.")
    print("It may also be that the host provided is wrong, be sure it is the appropriate one (usually localhost)\n")
    exit()

except mysql.connector.errors.ProgrammingError:
    print(bold + "MySQL credentials error" + end +
          ": The credentials provided (user, password, database) are not correct.\n")
    exit()

except:
    print("An error occured, check the code for an insight")
    exit()


def get_crypto_price(crypto=""):
    """ Get the current crypto exchange rate, using eur.rate.sx """

    URL = "https://eur.rate.sx/" + crypto
    response = requests.get(URL)

    return response


for source in portfolio:
    wallet = portfolio[source]
    print(source)

    for crypto in wallet.keys():
        response = get_crypto_price(str(wallet[crypto]) + crypto)

        if wallet[crypto] != 0.0:
            # the response has a \n character at the end, we strip it and format the output
            print("\t" + crypto + " -> " + response.text[:-1] + " €")
