'''
– [x] Read all the tickers from an input file (tickers.txt). The tickers are listed one per line.
– [x] Define a function that updates the current stock information for the ticker that is passed as an argument.
	The information is written and updated in an information file (say info.csv for example).
– [x] The module should call this function for each input ticker in tickers.txt file.
– [x] This module should run for specified time period, say time lim in seconds and update the data in the information file.
– [x] The information file should be a csv file, with the first row being the column headers. For each ticker in the tickers.txt
	file, the information file, should have one row for each minute.
– [] The Time column should contain time in the HH:MM format with HH ranging from 00 to 23. There should be one and only one row
	corresponding a specific value of Time and Ticker.
– [x] In order to extract the stock information for a ticker, say ”AAPL”, you should use the iex-api-python which is described here:
	https://pypi.org/project/iex-api-python/. You need to fetch the current data for the following fields: 
	low, high, open, close, latestPrice, latestVolume. 
	Use the quote() function of the Stock corresponding to the ticker.
– [x] The csv must have data in the format:
	Time, Ticker, latestPrice, latestVolume, Close, Open, low, high
– [x] Store the time of the query and the respective keys and values in the info.txt file. For each iteration, during which you save
	the data for a specific minute, you may wait till the start of the next minute, say, 12:37 and then save the data for all
	tickers during that iteration with the Time field set to the minute (12:37).
– [x] Please use the information on the API page to figure out how to install iex-api-python. The page also has the information for
	fetching necessary data about a stock ticker.
– [x] The arguments passed to this module are: time lim, ticker filename, info filename
'''

import sys
from iex import Stock
from datetime import datetime, time
import json
import csv
import pandas as pd
import asyncio
import aiohttp
import time

async def main():
	tasks = []
	res = []
	async with aiohttp.ClientSession() as session:
		for t in get_tickers(sys.argv[2]):
			tasks.append(fetch(session, t))
		quotes = await asyncio.gather(*tasks)
		for q in quotes:
			t = datetime.time(datetime.now()).isoformat(timespec='minutes')
			res.append([t, q['symbol'], q['latestPrice'], q['latestVolume'], q['close'], q['open'], q['low'], q['high']])
	return res

def get_tickers(fname):
	'''
		args:
			fname - file name of tickers file

		Takes the file name, opens it and returns the contents in a list
	'''
	with open(fname) as file:
		t = [line.strip("\n") for line in file]
	return t

def update_csv():
	pass

async def fetch(session, ticker):
	'''
		args:
			ticker - ticker symbol used to look up its stock info
			session - used in the async routine of calling the api

		Takes the ticker and looks up its stock info. 
		Info is fetched from the api and returned as a dict in json form

	'''	
	async with session.get(f'https://api.iextrading.com/1.0/stock/{ticker}/quote?displayPercent=false') as response:
		print(f'requesting {ticker}')
		return await response.json()

	# q = Stock(ticker).quote()
	# print(f'requesting {ticker} info')
	# q = Stock(ticker).quote()
	# print(f"got {ticker} quote!")
	# get current time

	# return need values and time
	# return [t, q['symbol'], q['latestPrice'], q['latestVolume'], q['close'], q['open'], q['low'], q['high']]

if __name__ == '__main__':
	header = ["Time", "Ticker", "latestPrice", "latestVolume", "Close", "Open", "low", "high"]
	# open csv
	final = pd.DataFrame([], columns=header)

	start_time = time.time()

	# fetches stcok info every minute until time limit is reached
	while (time.time() - start_time) < int(sys.argv[1]):
		df = pd.DataFrame(asyncio.run(main()), columns=header)
		final = final.append(df, ignore_index=True)
		print(time.time() - start_time)
		if (time.time() - start_time) > int(sys.argv[1]):
			break
		else:
			time.sleep(60)
	final.sort_values(by=['Ticker', 'Time'], inplace=True)
	print(final)
	final.to_csv('info.csv', index=False)










