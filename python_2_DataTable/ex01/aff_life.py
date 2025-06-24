import matplotlib.pyplot as plt
import pandas as pd
from load_csv import load


def display_graph(data: pd.DataFrame, country: str):
    assert isinstance(data, pd.DataFrame), "Please provide a Dataframe"
    assert not data.empty, "Dataframe is empty"
    country_data = data.loc[data["country"] == country]
    assert not country_data.empty, (
        "Data could not be loaded. Please check the dataset."
    )

    y = country_data.values[0][1:]
    x = country_data.columns[1:]

    plt.plot(x, y, label=country)
    plt.title(f"{country} Life expectancy Projections")
    plt.ylabel('Life expectancy')
    plt.xlabel('Year')
    plt.xticks(x[::40])
    plt.legend()
    plt.show()


def main():
    try:
        data = load("life_expectancy_years.csv")
        campus = input("In which country is your campus: ")
        display_graph(data, campus)
    except AssertionError as error:
        print(AssertionError.__name__ + ":", error)


if __name__ == "__main__":
    main()
