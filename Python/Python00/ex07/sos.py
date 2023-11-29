from sys import argv


NESTED_MORSE = {' ': '/',
                'A': '.-',
                'B': '-...',
                'C': '-.-.',
                'D': '-..',
                'E': '.',
                'F': '..-.',
                'G': '--.',
                'H': '....',
                'I': '..',
                'J': '.---',
                'K': '-.-',
                'L': '.-..',
                'M': '--',
                'N': '-.',
                'O': '---',
                'P': '.--.',
                'Q': '--.-',
                'R': '.-.',
                'S': '...',
                'T': '-',
                'U': '..-',
                'V': '...-',
                'W': '.--',
                'X': '-..-',
                'Y': '-.--',
                'Z': '--..',
                '1': '.----',
                '2': '..---',
                '3': '...--',
                '4': '....-',
                '5': '.....',
                '6': '-....',
                '7': '--...',
                '8': '---..',
                '9': '----.',
                '0': '-----',
                ',': '--..--',
                '.': '.-.-.-',
                '?': '..--..',
                '/': '-..-.',
                '-': '-....-',
                '(': '-.--.',
                ')': '-.--.-'
                }


def testValidArgument(text: str) -> bool:
    for c in text:
        if (not (c.isalnum() or c.isspace())):
            return False
    return True


def main():
    try:
        assert argv.__len__() == 2, "the arguments are bad"
        text = argv[1]
        assert testValidArgument(text),  "the arguments are bad"
        encoded = ''
        for c in text:
            encoded += NESTED_MORSE[c.upper()] + ' '
        print(encoded[:-1])
    except AssertionError as msg:
        print("AssertionError:", msg)
    except ValueError:
        print("ValueError: argument is not an integer")


if __name__ == "__main__":
    main()
