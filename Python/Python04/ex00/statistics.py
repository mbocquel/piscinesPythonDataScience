from typing import Any


def ft_statistics(*args: Any, **kwargs: Any) -> None:
    """My statistics function"""
    if (len(args) > 0):
        mean = sum(args) / len(args)
        median = sorted(args)[int(len(args)/2)]
        quartile = [float(sorted(args)[int(len(args)/4)]),
                    float(sorted(args)[int(3*len(args)/4)])]
        var = sum([(x - mean)**2 for x in args])/(len(args))
        std = var**(0.5)
    for key, value in kwargs.items():
        if (len(args) == 0):
            print("ERROR")
        else:
            match value:
                case 'mean':
                    print("mean :", mean)
                case 'median':
                    print("median :", median)
                case 'quartile':
                    print("quartile: ", quartile)
                case 'std':
                    print("std :", std)
                case 'var':
                    print("var :", var)
