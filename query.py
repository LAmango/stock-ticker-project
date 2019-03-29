'''
	– Define a function that takes the information file name, time and the ticker as the input and prints
		the details corresponding to a specific time and ticker symbol to the terminal. The data must be printed as follows:
		field 1: value 1
		field 2: value 2
		.
		.
		.
		field n: value n
	– The above function also takes a verbose flag, which when true, the number of rows and number of columns in the information
		file will be printed out as well as the names of the columns.
	– Should have a main that takes the following flags and calls the function to print the values: 
		verbose
		time (HH:MM format)
		file (information file that contains the information) 
		ticker
'''

import sys
import pandas as pd

# parse the flags entered from the command line. Sets key and value for each.
def parseCommandLineFlags():
	flag,value = [],[]

	for arg in sys.argv[1:]:
		if arg[0]=="-":
			flag.append(arg[1:])
		else:
			value.append(arg)

	flags = dict(list(zip(flag, value)))
	return flags

def str_to_bool(v):
    if v.lower() == "true": # set the verbose flag to lower case to check for true of false
        return True
    else:
        return False

# steps through file and collects information for requested ticker.
def query(verbose, file_name, ticker, time):

    df = pd.read_csv(file_name)
    rows = df.shape[0]
    columns = df.shape[1]

    df = df[(df["Ticker"] == ticker) & (df["Time"] == time)]
    cols = list(df)

    if str_to_bool(verbose):
        print("Number of rows:", rows)
        print("Number of columns:", columns)
        print("Column names:", cols)

    for col in cols:
        print(col + ":" + df[col].to_string(index=False))

if __name__ == "__main__":
    flags = parseCommandLineFlags()
    query(flags["verbose"], flags["file"], flags["ticker"], flags["time"])
    