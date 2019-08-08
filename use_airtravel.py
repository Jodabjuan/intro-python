"""
Use Flight Class
"""
from airtravel import Flight


def main():
    """
    Test function
    :return:
    """
    f = Flight("SN066")
    print(f.number())  # could use: Flight.number(f)  :(  :(
    f2 = Flight("FA044")
    print(f2.number(), f2.airline())


if __name__ == '__main__':
    main()
    exit(0)