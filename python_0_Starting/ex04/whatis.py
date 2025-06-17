import sys

try:
    n = len(sys.argv)
    assert n == 2, "Please provide one argument!"
    assert sys.argv[1].isdigit(), "Argument is not an integer"
    if (int(sys.argv[1]) % 2 == 0):
        print("I'm Even.")
    else:
        print("I'm Odd.")
except AssertionError as error:
    print("AssertionError:", error)
