from sys import argv

try:
    assert (argv.__len__() <= 2), "more than one argument is provided"
    if (argv.__len__() == 2):
        try:
            test = int(argv[1])
            if (test % 2 == 0):
                print("I'm Even")
            else:
                print("I'm Odd")
        except ValueError:
            assert False, "argument is not an integer"
except AssertionError as msg:
    print("AssertionError:", msg)
