"""
Use Flight Class
"""
from airtravel import Flight, Aircraft


def main():
    """
    Test function
    :return:
    """
    f = Flight("SN066")
    print(f.number())  # could use: Flight.number(f)  :(  :(
    f2 = Flight("FA044")
    print(f2.number(), f2.airline())

    a1 = Aircraft("G-EUP", "Airbus A319",
                  numrows=22, seatsper=6)
    print(a1.registration(), a1.model())


if __name__ == '__main__':
    main()
    exit(0)