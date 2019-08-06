"""
Learn about scoping in Python
L = local
E = enclosed
G = global
B = built-in
"""
count = 0 #global object


def show_count():
    """
    Display the current count
    :return: nothing
    """
    print(count)


def set_count(n):
    """
    Set the count to what I want
    :param n: input number
    :return: nothing
    """
    global count
    count = n


def main():
    """
    Test function
    :return: 
    """
    show_count()
    set_count(9)
    show_count()


if __name__ == '__main__':
    main()
    exit(0)