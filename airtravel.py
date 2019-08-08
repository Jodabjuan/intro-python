"""
An Flight Class. Model for aircraft flights
"""


class Flight:
    """
    A Flight with a particular passenger aircraft
    """
    def __init__(self, number, aircraft):
        """
        Initializes Flight number
        :param number: flight number
        :raises: ValueError (For invalid format)
        """
        # Validate flight number:
        # 5 digits  - AADDD  A=ALPHA  D=Digit
        if len(number) != 5:
            raise ValueError("Invalid Flight Number length."
                             .format(number))
        if not number[:2].isalpha():
            raise ValueError("No airline code ()"
                            .format(number))
        if not number[:2].isupper():
            raise ValueError("Invalid airline code ()"
                             .format(number))
        if not number[2:].isdigit():
            raise ValueError("Invalid route code ()"
                             .format(number))

        self._number = number
        self._aircraft = aircraft

        rows, seats = self._aircraft.seatplan()
        self._seating = [None] + [{letter: None for letter in seats} for _ in rows]

    def number(self):
        """
        flight number
        :return: flight number
        """
        return self._number[2:]

    def airline(self):
        return self._number[:2]




class Aircraft:

    def __init__(self, registration, model, numrows, seatsper):
        self._registration = registration
        self._model = model
        self._numrows = numrows
        self._seatsper = seatsper



    def registration(self):
        return self._registration

    def model(self):
        return self._model

    def numrows(self):
        return self._numrows

    def seatsper(self):
        return self._seatsper

    def seatplan(self):
        return(range(1, self._numrows +1), "ABCDEFGHJK"[:self._seatsper])






def main():
    """
    Test function
    :return:
    """
    pass


if __name__ == '__main__':
    main()
    exit(0)