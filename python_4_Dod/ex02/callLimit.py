def callLimit(limit: int):
    """
    Decorator to limit the number of times a function can be called.
    Args:
        limit (int): The maximum number of times the function can be called.
    Returns:
        A decorator that limits the number of calls to the decorated function.
    """
    count = 0

    def callLimiter(function):
        """
        Inner function that wraps the original function to
        enforce the call limit.
        Args:
            function: The function to be decorated.
        Returns:
            A wrapper function that checks the call count and
            raises an error if the limit is exceeded."""
        def limit_function(*args: any, **kwds: any):
            """
            Wrapper function that checks the call count and
            raises an error if the limit is exceeded.
            Args:
                *args: Variable length argument list for the function.
                **kwds: Keyword arguments for the function.
            Returns:
                The result of the original function if the
                call limit is not exceeded.
            """
            try:
                nonlocal count
                count += 1
                if count <= limit:
                    return function(*args, **kwds)
                else:
                    raise AssertionError(f"{function} call too many times")
            except AssertionError as error:
                print("Error:", error)
        return limit_function
    return callLimiter


def main():
    @callLimit(3)
    def f():
        print("f()")

    @callLimit(1)
    def g():
        print("g()")

    for i in range(3):
        f()
        g()


if __name__ == "__main__":
    main()
