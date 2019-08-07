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


def main():
    """
    Test function
    :return:
    """
    print(convert("11"))
    print(convert("Hello"))
    print(convert([1, 4, 8]))


if __name__ == '__main__':
    main()
    exit(0)
