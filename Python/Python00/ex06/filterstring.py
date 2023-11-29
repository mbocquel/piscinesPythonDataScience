from ft_filter import ft_filter
from sys import argv


def main():
    try:
        assert argv.__len__() == 3, "the arguments are bad"
        stringS = argv[1]
        intN = int(argv[2])
        print(ft_filter(lambda word: word.__len__() > intN,
                        stringS.split()))
    except AssertionError as msg:
        print("AssertionError:", msg)
    except ValueError:
        print("ValueError: argument is not an integer")


if __name__ == "__main__":
    main()
