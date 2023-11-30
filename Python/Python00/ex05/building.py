from sys import argv


def n_lower_chars(string):
    """Takes a string and return the number of lowercase chars in it."""
    return sum(1 for c in string if c.islower())


def n_upper_chars(string):
    """Takes a string and return the number of uppercase chars in it."""
    return sum(1 for c in string if c.isupper())


def n_space_chars(string):
    """Takes a string and return the number of whitespace chars in it."""
    return sum(1 for c in string if c.isspace())


def n_digit_chars(string):
    """Takes a string and return the number of digit chars in it."""
    return sum(1 for c in string if c.isdigit())


def n_punctuation_chars(string):
    """
    Takes a string and return the number of punctuation chars in it.
    """
    punctuation = "!\"#$%&'()*+,-./:;<=>]?@[\\^_`{|}~"
    return sum(1 for c in string if c in punctuation)


def main():
    try:
        assert argv.__len__() <= 2, "Too many arguments !"
        str = ""
        if (argv.__len__() == 1):
            try:
                str = input("What is the text to count?\n") + '\n'
            except EOFError:
                pass
        else:
            str = argv[1]
        print("The text contains", str.__len__(), "characters:")
        print(n_upper_chars(str), "upper letters")
        print(n_lower_chars(str),  "lower letters")
        print(n_punctuation_chars(str),  "punctuation marks")
        print(n_space_chars(str),  "spaces")
        print(n_digit_chars(str),  "digits")
    except AssertionError as msg:
        print(msg)


if __name__ == "__main__":
    main()
