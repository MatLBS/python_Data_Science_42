from ft_filter import ft_filter
import sys


def myfunc(n):
    """Return true if len of a is greater than n, which is the number the
    function was initialize with."""
    return lambda a: len(a) > n


def main(argv):
    assert (
        len(argv) == 3
        and type(argv[1]) is str
        and argv[2].isdigit()
    ), "the arguments are bad"
    words = argv[1].split()

    greaterLength = myfunc(int(argv[2]))
    newList = list(ft_filter(greaterLength, words))
    print(newList)


if __name__ == "__main__":
    try:
        main(sys.argv)
    except AssertionError as error:
        print("AssertionError:", error)
