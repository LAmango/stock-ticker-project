'''
	– [] Define a function that takes the information file name, a ticker, a column name (say col which is either
		latestPrice or latestVolume), a time range, t and a graph file name as the input.
	– [] The function is called by main, which accepts the arguments and passes those to the function.
	– [] The function must read the data from the information file, select the data for the specified ticker, 
		and train a machine learning based model to predict the value of the specified column for the next t minutes.
	– [] You should only use the Time column (you can split it into hours and minutes) to predict the value of col based
		on the historical data stored in the information file.
	– [] You must use the linear regression in sklearn.linear model to train using the historical data for the specific ticker 
		stored in the information file and then predict the result for the next t minutes.
	– [] You must also plot and save the plot for the historical variation in the value of col as well as the predicted values.
		The actual and predicted data should be plotted out on the same graph in two different colours.
'''
import sys
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

#python3 predictor.py info.csv FLWS latestPrice 5 g.txt
# only use time to train and use time to predict the next price or volume

def main(args):
	_, info_file, ticker, col, time_range, graph = args
	parse_args(info_file, ticker, col, time_range, graph)

def plot_graph(time, prediction, label, df, graph):
	# join the hour and minutes back together
	time = ["".join(i) for i in time]

	plt.plot(list(df['Time']), list(df[label]))
	plt.plot(time, prediction)
	plt.xlabel('Time')
	plt.ylabel(label)

	plt.tick_params(axis='x', rotation=45)
	plt.savefig(graph)

def parse_args(info_file, ticker, col, time_range, graph):
	df = pd.read_csv(info_file)
	indexes = df[df['Ticker'] != ticker].index
	df = df.drop(indexes)
	X = df['Time'].str.split(":", n = 1, expand = True)
	y = df[[col]]

	X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=1)

	regression_model = LinearRegression()
	regression_model.fit(X_train, y_train)

	time = [df.iloc[[-1]]['Time']]
	prediction = [float(df.iloc[[-1]][col])]

	# add the end of the historcal time to the beginning of predictive time
	# so that they connect on the graph
	hour = int(X.iloc[[-1]][0])
	minute = int(X.iloc[[-1]][1])

	# predict the next time_range minutes of the stock
	for i in range(int(time_range)):
		prediction.append(float(regression_model.predict([[hour,minute]])))
		minute += 1
		if minute == 60:
			minute = 0
			hour += 1
		time.append([str(hour), ":", str(minute).zfill(2)])
	plot_graph(time, prediction, col, df, graph)

if __name__ == '__main__':
	main(sys.argv)