from sys import argv

if (argv.__len__() > 2):
    print("AssertionError: more than one argument is provided")
elif (argv.__len__() == 2):
    try:
        test = int(argv[1])
        if (test % 2 == 0):
            print("I'm Even")
        else:
            print("I'm Odd")
    except ValueError:
        print("AssertionError: argument is not an integer")
