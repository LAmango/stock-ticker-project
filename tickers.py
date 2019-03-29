'''
	This module will require the following fuctions:

	1. save_tickers:
		args:
			n - int, the first n VALID tickers

		use the following url to access all tickers in the nasdaq
		https://www.nasdaq.com/screening/companies-by-industry.aspx?exchange=NASDAQ&render=download
		
		use the iex-api-python module to verify that the price function for the Stock
		corresponding to the fetched ticker works. if the .price() for a given ticker does not work,
		DO NOT have it written to the file.

		write one ticker symbole per line in a file called tickers.txt

		the 'n' argument will be provided as a system argument to the module.

		there should be a main() module that calls the save_ticker function and passes the value of 'n'
		to it. 

		value of n will be <= 150
'''

import re
import requests
from iex import Stock
import sys

# Checks to see if the price for the ticker is available.
def is_valid(symbol):
    try:
        Stock(symbol).price()
        return True
    except:
        return False

# Gathers stock tickers from nasdaq.com and collects up to 150.
def save_tickers(n, file_name):
    mylist = []
    counter = 0
    for x in range(1,5):
        content=requests.get("https://www.nasdaq.com/screening/companies-by-industry.aspx?exchange=NASDAQ&page=" + str(x))
        # REGEX to find stock symbol from page.
        mylist += re.findall(r'<a href="https://www.nasdaq.com/symbol/[^"/]+">\s+([A-Z]+)</a>',str(content.text))

    fp = open(file_name, "w")

    for i in mylist:
        if is_valid(i):
            fp.write(i + "\n")
            counter += 1
            if counter > n:
                break
            if counter == n:
                break
    fp.close()


if __name__ == "__main__":
    n = int(sys.argv[1])
    file_name = (sys.argv[2])
    save_tickers(n, file_name)
