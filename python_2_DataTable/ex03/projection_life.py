import matplotlib.pyplot as plt
import pandas as pd
from load_csv import load


def display_graph(life: pd.DataFrame, income: pd.DataFrame, date: str) -> None:
    """
    Displays a scatter plot of life expectancy against income for a given date.
    Args:
        life (pd.DataFrame): DataFrame containing life expectancy data.
        income (pd.DataFrame): DataFrame containing income data.
        date (str): The date for which to display the data.
    """
    life_date = life[date]
    income_date = income[date]

    assert not life_date.empty and not income_date.empty, (
        "Data could not be loaded. Please check the dataset."
    )

    plt.plot(income_date, life_date, "ob")
    plt.xlabel("Gross domectic product")
    plt.xscale('log')
    plt.xticks([300, 1000, 10000], ["300", "1k", "10k"])
    plt.ylabel("Life Expectancy")
    plt.title(f"{date}")
    plt.show()


def main():
    try:
        life = load("life_expectancy_years.csv")
        income = (
            load("income_per_person_gdppercapita_ppp_inflation_adjusted.csv")
        )
        display_graph(life, income, "1900")
    except AssertionError as error:
        print(AssertionError.__name__ + ":", error)


if __name__ == "__main__":
    main()
