'''
To show how references work
'''

def modify(k):
    """
    Modify the content of a list
    :param k: input list
    :return: nothing
    """

    # Lists are passed by refernece
    k.append(39)
    print("K = ", k)

def replace(g):
    """
    replace input list
    :param g: input list
    :return: nothing
    """
    g =[17, 48, 89]
    print ("G = ", g)

def main():
    """
    test function
    :return: nothing
    """
    m = [9, 15, 24]
    print("M-before = ", m)
    modify(m)
    print("M-after = ", m)
    replace(m)
    print("M-after Replace = ", m)


if __name__ == '__main__':
    main()
    exit(0)