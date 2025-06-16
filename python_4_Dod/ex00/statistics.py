def ft_statistics(*args: any, **kwargs: any) -> None:
    len_args = len(args)
    for kwarg in kwargs:
        if len_args == 0:
            print("ERROR")
            continue
        match kwargs[kwarg]:
            case "mean":
                mean = sum(args) / len_args
                print(mean)
            case "median":
                median = int(len_args / 2)
                print(sorted(args)[median])
            case "quartile":
                first_quart = int(len_args / 4)
                third_quart = int(len_args * 0.75)
                list_quart = [float(sorted(args)[first_quart]), float(sorted(args)[third_quart])]
                print(list_quart)
            case "std":
                mean = sum(args) / len_args
                sum_square = 0
                for x in args:
                    sum_square += (x - mean)**2
                std = (sum_square / len_args)**(1/2)
                print(std)
            case "var":
                mean = sum(args) / len_args
                sum_square = 0
                for x in args:
                    sum_square += (x - mean)**2
                var = sum_square / len_args
                print(var)
            case _:
                assert "Error"


def main():
    try:
        ft_statistics(1, 42, 360, 11, 64, toto="mean", tutu="median", tata="quartile")
        print("-----")
        ft_statistics(5, 75, 450, 18, 597, 27474, 48575, hello="std", world="var")
        print("-----")
        ft_statistics(5, 75, 450, 18, 597, 27474, 48575, ejfhhe="heheh", ejdjdejn="kdekem")
        print("-----")
        ft_statistics(toto="mean", tutu="median", tata="quartile")
    except AssertionError as error:
        print(error)


if __name__ == "__main__":
    main()
