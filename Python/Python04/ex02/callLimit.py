from typing import Any


def callLimit(limit: int):
    """Decorator that store the number of time the functon has been called """
    count = 0

    def callLimiter(function):
        """Decorator that limit the call of function"""
        def limit_function(*args: Any, **kwds: Any):
            """Warpped function"""
            nonlocal count
            count += 1
            if (count <= limit):
                val = function(*args, **kwds)
                return val
            else:
                print(f"Error: {function} call too many times")
        return limit_function
    return callLimiter
