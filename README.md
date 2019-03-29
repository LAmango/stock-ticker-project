# stock-ticker-project

**tickers.py**
* This is module will crawl a webpage to aquire *n* number of tickers
* Execution instuction is the following:
> ```python3 tickers.py number_of_tickers ticker_file```

**fetcher.py**
* Will take the iex module to lookup the Stock info and parese the info needed.
* That info will then be saved in a .csv file
* Execution instruction is the following:
> ```python3 fetcher.py time_lim ticker_filename info_filename```

**query.py**
* Reads the info file and looks up a specific time and ticker within the info file.
* Exectution instrustion is the following:
> ```python3 query.py -verbose True/False -file info_filename -ticker ticker -time time```

**predictor.py**
* Takes a ticker that is in the info file.
* Trains a model with the time and specified value (latestPrice/latestVolume)
* Plots the info and predictions on a graph and saves it.
* Exectution instrustion is the following:
> ```python3 predictor.py ticker info_filename graph_filename col time_in_minutes```