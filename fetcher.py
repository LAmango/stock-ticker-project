'''
– Read all the tickers from an input file (tickers.txt). The tickers are listed one per line.
– Define a function that updates the current stock information for the ticker that is passed as an argument.
	The information is written and updated in an information file (say info.csv for example).
– The module should call this function for each input ticker in tickers.txt file.
– This module should run for specified time period, say time lim in seconds and update the data in the information file.
– The information file should be a csv file, with the first row being the column headers. For each ticker in the tickers.txt
	file, the information file, should have one row for each minute.
– The Time column should contain time in the HH:MM format with HH ranging from 00 to 23. There should be one and only one row
	corresponding a specific value of Time and Ticker.
– In order to extract the stock information for a ticker, say ”AAPL”, you should use the iex-api-python which is described here:
	https://pypi.org/project/iex-api-python/. You need to fetch the cur- rent data for the following fields: 
	low, high, open, close, latestPrice, latestVolume. 
	Use the quote() function of the Stock corresponding to the ticker.
– The csv must have data in the format:
	Time, Ticker, latestPrice, latestVolume, Close, Open, low, high
– Store the time of the query and the respective keys and values in the info.txt file. For each iteration, during which you save
	the data for a specific minute, you may wait till the start of the next minute, say, 12:37 and then save the data for all
	tickers during that iteration with the Time field set to the minute (12:37).
– Please use the information on the API page to figure out how to install iex-api-python. The page also has the information for
	fetching necessary data about a stock ticker.
– The arguments passed to this module are: time lim, ticker filename, info filename
'''