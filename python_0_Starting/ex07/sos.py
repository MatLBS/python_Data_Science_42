import sys


def main(argv):
    """
    Take a string as parameter and encodes it into Morse Code
    """
    NESTED_MORSE = {
        'A': '.-',		'B': '-...',	'C': '-.-.',
        'D': '-..',		'E': '.',		'F': '..-.',
        'G': '--.',	'	H': '....',		'I': '..',
        'J': '.---',	'K': '-.-',		'L': '.-..',
        'M': '--',	 	'N': '-.',	 	'O': '---',
        'P': '.--.',	'Q': '--.-',	'R': '.-.',
        'S': '...',		'T': '-',		'U': '..-',
        'V': '...-',	'W': '.--',		'X': '-..-',
        'Y': '-.--',	'Z': '--..',
        '0': '-----',	'1': '.----',	'2': '..---',
        '3': '...--',	'4': '....-',	'5': '.....',
        '6': '-....',	'7': '--...',	'8': '---..',
        '9': '----.',	' ': '/ '
    }

    assert len(argv) == 2, "you must provide one argument"
    str = argv[1]
    newStr = ""
    for i in range(len(str)):
        assert str[i].upper() in NESTED_MORSE, "the arguments are bad"
        newStr += NESTED_MORSE[str[i].upper()] + " "
    print(newStr)


if __name__ == "__main__":
    try:
        main(sys.argv)
    except AssertionError as error:
        print("AssertionError:", error)
