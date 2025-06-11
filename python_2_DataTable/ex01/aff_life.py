import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from load_csv import load

def display_graph(data: pd.DataFrame, country: str):
	country_data = data.loc[data["country"] == country]
	assert country_data is not None, "Data could not be loaded. Please check the dataset."

	y = country_data.values[0][1:]
	x = country_data.columns[1:]

	plt.plot(x, y, label=country)
	plt.title("France Life expectancy Projections")
	plt.ylabel('Life expectancy')
	plt.xlabel('Year')
	plt.xticks(x[::40])
	plt.legend()
	plt.show()

def main():
	try:
		data = load("life_expectancy_years.csv")
		display_graph(data, "France")
	except AssertionError as error:
		print(AssertionError.__name__ + ":", error)


if __name__ == "__main__":
	main()