'''
	This module will require the following fuctions:

	1. save_tickers:
		args:
			n - int, the first n VALID tickers

		use the following url to access all tickers in the nasdaq
		http://www.nasdaq.com/screening/companies-by-industry.aspx?exchange=NASDAQrender=download
		
		use the iex-api-python module to verify that the price function for the Stock
		corresponding to the fetched ticker works. if the .price() for a given ticker does not work,
		DO NOT have it written to the file.

		write one ticker symbole per line in a file called ticker.txt

		the 'n' argument will be provided as a system argument to the module.

		there should be a main() module that calls the save_ticker function and passes the value of 'n'
		to it. 

		value of n will be <= 150
'''