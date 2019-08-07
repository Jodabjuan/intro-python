"""
Learn about handling exceptions (<> normal flow of program ) errors...
"""
import sys


def convert(s):
    """
    converts a string to integer
    :param s:
    :return:
    """
    try:
        return int(s)
    except (ValueError, TypeError) as e:
        print("Conversion Error {}".format(str(e)), file=sys.stderr)
    return -1


def sqrt(x):
    """
    Compute the square root using the method Heron of Alex
    :param x: Number to compute the sqrt
    :return: sqrt of x
    """
    guess = x
    i = 0
    try:
        while guess*guess != x and i < 20:
            guess = (guess + x/guess)/2.0
            i += 1
    except ZeroDivisionError:
        raise ValueError()

    return guess



def main():
    """
    Test function
    :return:
    """
    # print(convert("11"))
    # print(convert("Hello"))
    # print(convert([1, 4, 8]))
    print(sqrt(9))
    print(sqrt(11))
    print(sqrt(-1))


if __name__ == '__main__':
    main()
    exit(0)
