"""
Use Flight Class
"""
from airtravel import Flight, Aircraft
from pprint import pprint as pp

def main():
    """
    Test function
    :return:
    """
    f1 = Flight("SN066")
    print(f1.number(), f1.airline())  # could use: Flight.number(f)  :(  :(
    f2 = Flight("FA044")
    print(f2.number(), f2.airline())

    a1 = Aircraft("G-EUP", "Airbus A319",
                  numrows=22, seatsper=6)
    print(a1.registration(), a1.model())
    pp(a1._seating)


if __name__ == '__main__':
    main()
    exit(0)