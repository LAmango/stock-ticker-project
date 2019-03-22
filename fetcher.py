'''
– [x] Read all the tickers from an input file (tickers.txt). The tickers are listed one per line.
– [] Define a function that updates the current stock information for the ticker that is passed as an argument.
	The information is written and updated in an information file (say info.csv for example).
– [x] The module should call this function for each input ticker in tickers.txt file.
– [] This module should run for specified time period, say time lim in seconds and update the data in the information file.
– [] The information file should be a csv file, with the first row being the column headers. For each ticker in the tickers.txt
	file, the information file, should have one row for each minute.
– [x] The Time column should contain time in the HH:MM format with HH ranging from 00 to 23. There should be one and only one row
	corresponding a specific value of Time and Ticker.
– [x] In order to extract the stock information for a ticker, say ”AAPL”, you should use the iex-api-python which is described here:
	https://pypi.org/project/iex-api-python/. You need to fetch the current data for the following fields: 
	low, high, open, close, latestPrice, latestVolume. 
	Use the quote() function of the Stock corresponding to the ticker.
– [] The csv must have data in the format:
	Time, Ticker, latestPrice, latestVolume, Close, Open, low, high
– [] Store the time of the query and the respective keys and values in the info.txt file. For each iteration, during which you save
	the data for a specific minute, you may wait till the start of the next minute, say, 12:37 and then save the data for all
	tickers during that iteration with the Time field set to the minute (12:37).
– [x] Please use the information on the API page to figure out how to install iex-api-python. The page also has the information for
	fetching necessary data about a stock ticker.
– [] The arguments passed to this module are: time lim, ticker filename, info filename
'''

import sys
from iex import Stock
import pandas
from datetime import datetime, time
import json
import csv

def get_tickers(fname):
	'''
		args:
			fname - file name of tickers file

		Takes the file name, opens it and returns the contents in a list
	'''
	with open(fname) as file:
		t = [line.strip("\n") for line in file]
	return t

def update_csv(ticker):
	'''
		args:
			ticker - ticker symbol used to look up its stock info

		Takes the ticker and looks up its stock info. 
		Then info is updated to a csv file

	'''	


	q = Stock(ticker).quote()

	# get current time
	t = datetime.time(datetime.now()).isoformat(timespec='minutes')

	# add the needed values to a list
	return [t, q['symbol'], q['latestPrice'], q['latestVolume'], q['close'], q['open'], q['low'], q['high']]

	


if __name__ == '__main__':
	header = ["Time", "Ticker", "latestPrice", "latestVolume", "Close", "Open", "low", "high"]
	# open csv
	with open(sys.argv[2], 'w') as info:
		wtr = csv.writer(info)
		wtr.writerow(header)
		for t in get_tickers(sys.argv[1]):
			wtr.writerow(update_csv(t))











