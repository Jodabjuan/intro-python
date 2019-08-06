"""
Learn about collections:  Tuples, Strings, Ranges, List, Dictionaries and sets
"""


def do_tuples():
    """
    practice tuples
    :return: nothing
    """
    # Immutable sequence of arbitrary objects
    # use () to define a tuple
    t = ("Ogden", 1.99, 2)
    print(t, type(t))
    print("Size ", len(t))
    print("one object - ", t[0])
    for item in t:
        print(item)
    # Single tuples, must end with a comma
    t1 = (6, )
    print(t1, type(t1))
    # Tuple does not require (   )
    t2 = 1, 2, 3, 5
    print(t2, type(t2))
    t_from_1 = tuple(3,77,1)
    print(t_from_1, type(t_from_1))
    print(5 in (3, 6, 8, 5, 12))
    print(5 not in (3, 6, 8, 5, 12))


def min_max(items):
    """
    returns the min and max if a collection
    :param items: collection
    :return: min and max
    """
    return min(items), max(items)


def swap(x1, x2):
    """
    Swapps two values in a tuple
    :param x1: first value to swap
    :param x2: second value to swap
    :return:
    """
    return x2, x1



def main():
    """
    Test function
    :return: 
    """
    # do_tuples()
    # output = min_max([56, 79, 11, 12, 90])
    # print("min = ", output[0])
    # print("max = ", output[1])
    #  tuple unpacking example
    # lower, upper = min_max([56, 79, 11, 12, 90])
    # print("min = ", lower)
    # print("max = ", upper)
    # swap values
    # a = "jelly"
    # b = "bean"
    # print(a + " " + b)
    # a, b = swap(a, b)
    # print(a + " " + b)
    # a, b = b, a
    # print(a, b)
    do_tuples()

if __name__ == '__main__':
    main()
    exit(0)