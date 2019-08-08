"""
Use Flight Class
"""
from airtravel import Flight, Aircraft
from pprint import pprint as pp


def make_flight():
    numrows = 22
    seatsper = 6
    flight = Flight("SN066",
                Aircraft("G-EUP",
                         "Airbus A319",
                         numrows,
                         seatsper))
    # pp(f1._seating)
    flight.allocates("12E", "Guide Van Rosen")
    flight.allocates("12B", "Sam Shafter")
    flight.allocates("20E", "Jimmy Hancock")
    flight.allocates("05A", "Del Ray Bell")
    flight.allocates("12C", "Brent Timothy")
    return flight


def console_card_printer(passenger, seat, flight_number, aircraft):
    output = "| Name:  {0}"  \
             " Flight:  {1} "  \
             " Seat:   {2}"    \
             " Aircraft:  {3}"  \
             " |".format(passenger, flight_number, seat, aircraft)
    banner = "+" + "-" * (len(output) - 2) + "+"
    border = "|" + " " * (len(output) - 2) + "|"
    lines = [banner, border, output, border, banner]
    card = '\n'.join(lines)
    print(card)
    print()

def main():
    """
    Test function
    :return:
    """

    flight_1 = make_flight()
    # pp(flight_1._seating)
    flight_1.make_boarding_class(console_card_printer)
    print("Number of Available Seats", flight_1.num_available_seats())



if __name__ == '__main__':
    main()
    exit(0)