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


# Database connection.
# We have to make sure it does connect, otherwise give hints on why not.
try:
    mydb = mysql.connector.connect(
        host=creds[0],
        user=creds[1],
        password=creds[2],
        database=creds[3]
    )

    query = "SELECT * FROM my_money;"
    portfolio = get_portfolio(*query_database(mydb, query))

except mysql.connector.errors.InterfaceError:
    print(bold + "MySQL connection Error:" + end +
          " MySQL is probably not running. Please start it, with\n\tsudo systemctl start mysql\nif you are running a modern Linux system.")
    print("It may also be that the host provided is wrong, be sure it is the appropriate one (usually localhost)\n")
    exit()

except mysql.connector.errors.ProgrammingError:
    print(bold + "MySQL credentials error:" + end +
          " The credentials provided (user, password, database) are not correct.\n")
    exit()

except:
    print("An error occured, check the code for an insight")
    exit()


def get_crypto_price(crypto=""):
    """ Get the current crypto exchange rate, using eur.rate.sx """

    URL = "https://eur.rate.sx/" + crypto
    response = requests.get(URL)

    # The response has a \n character at the end, we strip it and format the output
    return response.text[:-1]


# Loop over each wallet, displaying and storing the values, converted to EUR
balance = {}
for source in portfolio:
    wallet = portfolio[source]
    print(bold + source + end)

    balance[source] = 0

    for crypto in wallet.keys():

        if wallet[crypto] != 0.0:

            response = get_crypto_price(str(wallet[crypto]) + crypto)

            try:
                amount = float(response)
                balance[source] += amount
            except ValueError:
                print("\t" + crypto +
                      ": there's no conversion rate available for such cryptocoin, in eur.rate.sx.")
                continue

            print("\t" + crypto + " -> " +
                  str(round(amount, 3)) + " €")
    print()

# Sum all within a wallet
[print(bold + source + " total: " + end + str(round(balance[source], 3)) + " €")
 for source in balance]

print()

# Sum all
print(bold + "Total, total: " + end +
      str(round(sum(balance.values()), 3)) + " €")
