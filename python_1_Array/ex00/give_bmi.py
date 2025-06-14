def give_bmi(
        height: list[int | float],
        weight: list[int | float]
) -> list[int | float]:
    """
    This function calculates the Body Mass Index (BMI)
    for each pair of height and weight.
    Args:
        height (list[int | float]): A list of heights in meters.
        weight (list[int | float]): A list of weights in kilograms.
    Returns:
        list[int | float]: A list of BMI values calculated as
        weight divided by the square of height.
    """
    assert len(height) == len(weight), (
        "Height and weight lists must be of the same length."
    )
    assert all(isinstance(item, (int, float)) for item in height), (
        "All height values must be integers or floats."
    )
    assert all(isinstance(item, (int, float)) for item in weight), (
        "All weight values must be integers or floats."
    )

    bmi = []
    for i in range(len(weight)):
        bmi.append(weight[i] / (height[i]**2))

    return bmi


def apply_limit(
    bmi: list[int | float],
    limit: int
) -> list[bool]:
    """
    This function checks if each BMI value is above a specified limit.
    Args:
        bmi (list[int | float]): A list of BMI values.
        limit (int): The limit to compare against.
    Returns:
        list[bool]: A list of boolean values indicating whether
        each BMI is above the limit.
    """
    assert all(isinstance(item, (int, float)) for item in bmi), (
        "All bmi values must be integers or floats."
    )
    assert type(limit) is int, "Limit value must be an integer."

    limit_list = []
    for i in range(len(bmi)):
        limit_list.append(True if bmi[i] >= limit else False)
    return limit_list


def main():
    try:
        height = [2.71, 1.15]
        weight = [165.3, 38.4]
        bmi = give_bmi(height, weight)
        print(bmi, type(bmi))
        print(apply_limit(bmi, 26))
    except AssertionError as error:
        print("AssertionError:", error)


if __name__ == "__main__":
    main()
