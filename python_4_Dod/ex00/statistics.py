def ft_statistics(*args: any, **kwargs: any) -> None:
    """
    Function that calculates statistics based on the provided arguments.
    Args:
        *args: Variable length argument list containing numerical values.
        **kwargs: Keyword arguments that specify the type
        of statistics to calculate.
        Valid keys are "mean", "median", "quartile", "std", and "var".
    """
    assert all(isinstance(arg, (int, float)) for arg in args), (
        "Values must be int or float"
    )

    len_args = len(args)
    for kwarg in kwargs:
        if len_args == 0:
            print("ERROR")
            continue
        match kwargs[kwarg]:
            case "mean":
                mean = sum(args) / len_args
                print(f"mean : {mean}")
            case "median":
                sorted_args = sorted(args)
                mid = len_args // 2
                if len_args % 2 == 0:
                    median = (
                        float((sorted_args[mid - 1] + sorted_args[mid]) / 2)
                    )
                else:
                    median = float(sorted_args[mid])
                print(f"median : {median}")
            case "quartile":
                first_quart = int(len_args / 4)
                third_quart = int(len_args * 0.75)
                list_quart = [
                    float(sorted(args)[first_quart]),
                    float(sorted(args)[third_quart])
                ]
                print(f"quartile : {list_quart}")
            case "std":
                mean = sum(args) / len_args
                sum_square = 0
                for x in args:
                    sum_square += (x - mean)**2
                std = (sum_square / len_args)**(1/2)
                print(f"std : {std}")
            case "var":
                mean = sum(args) / len_args
                sum_square = 0
                for x in args:
                    sum_square += (x - mean)**2
                var = sum_square / len_args
                print(f"var : {var}")


def main():
    try:
        ft_statistics(
            1, 42, 360, 11, 64, toto="mean", tutu="median", tata="quartile"
        )
        print("-----")
        ft_statistics(
            5, 75, 450, 18, 597, 27474, 48575, hello="std", world="var"
        )
        print("-----")
        ft_statistics(
            5, 75, 450, 18, 597, 27474, 48575,
            ejfhhe="heheh", ejdjdejn="kdekem"
        )
        print("-----")
        ft_statistics(toto="mean", tutu="median", tata="quartile")
    except (AssertionError, ValueError) as error:
        print(error)


if __name__ == "__main__":
    main()
