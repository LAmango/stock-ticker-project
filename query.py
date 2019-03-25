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

#query.py: A .py file for the Query module. To execute this, the command used will be:
# python3 query.py -verbose True -file info_filename -ticker ticker -time 13:33 

def parseCommandLineFlags():
	flag,value = [],[]

	for arg in sys.argv[1:]:
		if arg[0]=="-":
			flag.append(arg[1:])
		else:
			value.append(arg)

	flags = dict(list(zip(flag, value)))
	return flags

def isVerbose():
	return flags["verbose"]=="True"

def query(verbose, file_name, ticker, time):
	print(verbose)
	print(file_name)
	print(ticker)
	print(time)

if __name__ == "__main__":
    flags = parseCommandLineFlags()
    query(bool(flags["verbose"]), flags["file"], flags["ticker"], flags["time"])
    