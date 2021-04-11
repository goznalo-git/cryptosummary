# Cryptocurrency summary

This little, fun project is something like a Python parser for cryptocurrencies, a CLI summary and balance of each and all of them.

There are three parts in this project: storing the cryptocurrencies, fetching them and converting them using the current exchange rate.

## Storage 

-- WIP --

I´ve chosen a MySQL database as the means of storing the cryptocoins that I possess. 

Admittedly, this is probably the worst solution one can ever imagine to store this information. Changing the amount of cryptocoins is quite cumbersome, but I thought it would be more interesting, providing a cool project. Besides, I do not usually trade mine, hence the database will not need to be changed often

-- WIP --

## Fetch

This part entails querying the database to obtain the stored values, for their later conversion. It will be handled by Python, using the MySQL connector. In order to access the database, some credentials (host, username, password, database) are needed. I will have them written in a `credentials.txt` file, not included in the repository.




## Convert

For this we will use the terminal-based website `rate.sx` (or rather, its euro alternative `eur.rate.sx`). We can use the request module to get exchange rates. For instance, if we have 10 bitcoin we can get its euro value requesting the `eur.rate.sx/10btc` website.

We will incorporate this step in the same Python script as before.
