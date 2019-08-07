"""
An unordered collection of unique, immutable objects
Define it using {} - like dict but no key needed
You can use the set {} constructor to create one
"""



def main():
    """
    Test function
    :return:
    """
    p = {6, 78, 21, 45}
    print(p, type(p))
    data = [1, 3, 5, 2, 88, 3, 5]
    print(data, type(data))
    # eliminate duplicates
    sdata = set(data)
    print(sdata, type(sdata))




if __name__ == '__main__':
    main()
    exit(0)