'''
	– Define a function that takes the information file name, a ticker, a column name (say col which is either
		latestPrice or latestVolume), a time range, t and a graph file name as the input.
	– The function is called by main, which accepts the arguments and passes those to the function.
	– The function must read the data from the information file, select the data for the specified ticker, 
		and train a machine learning based model to predict the value of the specified column for the next t minutes.
	– You should only use the Time column (you can split it into hours and minutes) to predict the value of col based
		on the historical data stored in the information file.
	– You must use the linear regression in sklearn.linear model to train using the historical data for the specific ticker 
		stored in the information file and then predict the result for the next t minutes.
	– You must also plot and save the plot for the historical variation in the value of col as well as the predicted values.
		The actual and predicted data should be plotted out on the same graph in two different colours.
'''