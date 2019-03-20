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

# Currently pulls all stock information from website and prints it to screen
url = 'https://www.nasdaq.com/screening/companies-by-industry.aspx?exchange=NASDAQ&render=download'
response = requests.get(url)

# TODO: send output to file
if response.status_code == 200:
    print(response.content.decode('utf-8'))

else:
    print(response.status_code)