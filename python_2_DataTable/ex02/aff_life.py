import matplotlib.pyplot as plt
import pandas as pd
from load_csv import load


def normalize_population(pop_str) -> float:
    """
    Preprocesses the population string to convert it into
    a numeric value in standard form.

    Args:
        pop_str (str): Population string.

    Returns:
        float: Numeric population value.
    """
    if pop_str.endswith("M"):
        return float(pop_str[:-1]) * 1e6
    elif pop_str.endswith("k"):
        return float(pop_str[:-1]) * 1e3
    elif pop_str.endswith("B"):
        return float(pop_str[:-1]) * 1e9
    else:
        return float(pop_str)


def display_country(data: pd.DataFrame, color: str, country: str) -> None:
    """
    Displays the population data for a specific country.
    Args:
        data (pd.DataFrame): DataFrame containing population data.
        color (str): Color for the plot line.
        country (str): Name of the country to display.
    """
    years = data.columns[1:-50]
    data_values = data.values[0][1:-50]
    population = [normalize_population(pop) for pop in data_values]
    plt.plot(years, population, label=country, color=color)


def display_graph(
    data: pd.DataFrame,
    campus_country: str,
    other_country: str
) -> None:
    """
    Displays the population projections for two countries.
    Args:
        data (pd.DataFrame): DataFrame containing population data.
        campus_country (str): Name of the campus country.
        other_country (str): Name of the other country.
    """
    assert isinstance(data, pd.DataFrame), "Please provide a Dataframe"
    assert not data.empty, "Dataframe is empty"
    campus_country_data = data[data["country"] == campus_country]
    other_country_data = data[data["country"] == other_country]
    assert not campus_country_data.empty and not other_country_data.empty, (
        "Data could not be loaded. Please check the dataset."
    )

    display_country(other_country_data, "blue", other_country)
    display_country(campus_country_data, "green", campus_country)

    years = data.columns[1:-50:40]
    plt.xlabel('Year')
    plt.xticks(years)
    plt.ylabel('Population')
    plt.yticks([20000000, 40000000, 60000000], ["20M", "40M", "60M"])
    plt.legend(loc="lower right")
    plt.title(
        f"Population Projections in {campus_country} and {other_country}"
    )
    plt.show()


def main():
    try:
        data = load("population_total.csv")
        campus_country = input("In which country is your campus: ")
        other_country = input("Enter another country: ")
        display_graph(data, campus_country, other_country)
    except AssertionError as error:
        print(AssertionError.__name__ + ":", error)


if __name__ == "__main__":
    main()
