"""
Learn about references and passing variables
"""


def egg(var):
    """
    returns a variable bact to the user
    :param var: input object
    :return: input object
    """
    return var

# Required parameters must come first.
# Optional parameters after required parameters.
def sum_two(num1, num2 = 8):
    """
    Sum of two input integer objects
    :param num1: object 1
    :param num2: object 2 (optional, default =8)
    :return: sum of objects
    """
    total = num1 + num2
    print(num1, " + ", num2, " = ", total)
    return total


def banner(message, border = "*"):
    """
    :param message: message banner
    :param border: character to use for border
    :return: message with border
    """
    pass


def main():
    """
    Test function
    :return:
    """
    c = [6, 10, 20]
    e = egg(c)
    print(c is e)

    n1 = 3
    n2 = 9
    sum_two(n1, n2)
    sum_two(n1)


if __name__ == '__main__':
    main()
    exit(0)