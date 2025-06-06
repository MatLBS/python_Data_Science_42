import sys

try:
  n = len(sys.argv)
  assert n == 2, "Please provide one argument!"
  if (int(sys.argv[1]) % 2 == 0):
    print("I'm Even.")
  else:
    print("I'm Odd.")
except AssertionError as error:
    print("AssertionError:", error)
