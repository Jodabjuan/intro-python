"""
Learn more about strings
"""


def main():
    """
    Test function
    :return: 
    """
    s1 = "This is super cool"
    print("Size of s1: ", len(s1))
    # concatenation "+"
    s2 = "Weber " + "State " + "University"
    print(s2)
    # join method to connect large strings instead of "+"
    teams = ["Real Madrid", "Barcelona", "Manchester United"]
    record = ":".join(teams)
    print(record)
    print("Split Record: ", record.split(":"))
    # Partitioning Strings
    departure, _, arrival = "London:Edinburgh".partition(":")
    # the "_" underscore is a dummy object
    print(departure, arrival)
    # String formating using format() method
    print("The age of {0} is {1}".format("mario", 34))
    print("The age of {0} is {1}, and the birthday of {0} is {2}".format(
        "Mario", 34, "August 12th"))
    # Omitting the index
    print("The best numbers are {} and {}".format(4, 22))
    # by field name
    print("Current position {latitude} {longitude}".format(latitude="60N", longitude="5E"))
    # print elements of list
    print("Galactic position x={pos[0]}, y={pos[1]}, z={pos[2]}".format(pos=(85.6, 23.3, 99.0)))
    # Second version of "format" : print(f"(var)")   python 3.7
    # fname = "Waldo"
    #lname = "Weber"
    #print(f"the WSU mascot is {fname} {lname}")


if __name__ == '__main__':
    main()
    exit(0)