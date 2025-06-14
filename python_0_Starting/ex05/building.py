import sys


def main(argv):
    """This function takes a single string as argument and displays
    the sums of its upper-case characters, lower-case
    characters, punctuation characters, digits and spaces."""
    upper = lower = char = punc = digits = spaces = 0
    if argv is None or len(argv) == 1:
        print("Please provide a string:")
        str = input()
    else:
        str = argv[1]
        n = len(argv)
        assert n <= 2, "Please provide only one argument"

    for i in range(len(str)):
        if str[i] == ' ':
            spaces += 1
        elif str[i].islower():
            lower += 1
        elif str[i].isupper():
            upper += 1
        elif str[i].isdigit():
            digits += 1
        elif str[i] in "'.,;:?!-":
            punc += 1
        char += 1

    print("The text contains", char, "characters:")
    print(upper, "upper letters")
    print(lower, "lower letters")
    print(punc, "punctuation marks")
    print(spaces, "spaces")
    print(digits, "digits")


if __name__ == "__main__":
    try:
        main(sys.argv)
    except AssertionError as error:
        print("AssertionError:", error)
