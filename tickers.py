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

		write one ticker symbole per line in a file called ticker.txt

		the 'n' argument will be provided as a system argument to the module.

		there should be a main() module that calls the save_ticker function and passes the value of 'n'
		to it. 

		value of n will be <= 150
'''

import json
import requests
import pandas


def save_tickers(n):
    # Sets URL for stock information to pull from
    url = 'https://www.nasdaq.com/screening/companies-by-industry.aspx?exchange=NASDAQ&render=download'
    response = requests.get(url)

    if response.status_code == 200:
        # pulls all data from CSV file into string
        content = response.content.decode('utf-8')

        # splits string into a list at the newline feed from CSV info
        lines = content.split("\n")


        first_line = True

        # TODO: needs to check each symbol to see if price will be true.
        for line in lines:
            if first_line == False: # check to see if we are currently on the first line
                # create ticker file if needed, write to file
                fp = open("ticker.txt", "w")
                fp.write(content)
            else:
                # if we are on the first line, need to skip it and write the rest into file
                first_line = False

    else:
        print(response.status_code)


if __name__ == "__main__":
    n = 20
    save_tickers(n)