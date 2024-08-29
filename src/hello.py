"""
A python module containing a function that says hello!
"""

def hello(name: str = "World") -> None:
    """
    Prints a greeting to *name*.

    :param name: the name of the person to greet.

    >>> hello()
    Hello World!

    >>> hello("Fishy")
    Hello Fishy!
    """
    print(f"Hello {name}!")


if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
        hello(' '.join(sys.argv[1:]))
    else:
        hello()
