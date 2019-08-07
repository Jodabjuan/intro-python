"""
Learn more about lists
"""


def main():
    """
    Test function
    :return:
    """
    s = "Show how to do it".split( )
    print(s, type(s))
    # Access by index
    print("s[3] = ", s[3])
    print("Last memger: ", s[len(s)-1])  # VERY un-pythonic
    # use negative index
    print("s[-1] = ", s[-1])
    # Slicing
    print("From second member to one before the last member: ", s[1:-1])
    print("From second member to third member: ", s[1:3])
    print("From third member to the end: ", s[2:])
    print("From start to third member: ", s[:3])
    print("From start to the end: ", s[:])
    # Make a copy of the list
    t = s  # shallow copy (reference)
    print("s: ", s)
    print("t: ", t)
    print("t is s: ",t is s)
    t = s[:]  # new copy of info - not linked (deep copy)
    # or this
    # t = s.copy()
    # or this
    # t = list(s)
    print("t is s: ",t is s)
    print("t == s: ", t == s)   # compares values, not pointer address
    # Shallow copies
    # A list of lists
    a = [[1,2], [3,4]]  # is the same as a two dimensional array
    print(a, type(a))
    print("a[0]: ",a[0])
    print("a[0][1]: ", a[0][1])
     # Copy  the list of lists
    b = a[:]
    print("b is a: ", b is a)
    print("a[0] : ", a[0])
    print("b[0] : ", b[0])
    print("b[0] is a[0]: ", b[0] is a[0])
    a[0] = [5, 6]
    print("Changed a[0] to [5, 6]")
    print("b is a: ", b is a)
    print("a[0] : ", a[0])
    print("b[0] : ", b[0])
    print("b[0] is a[0]: ", b[0] is a[0])
    print("b[1] is a[1]: ", b[1] is a[1])

    # Modify a[1]
    a[1].append(5)
    print(a[1])
    print("b[1] is a[1]: ", b[1] is a[1])
    print("a: ", a)
    print("b: ", b)

    # Repetition
    c = [21, 37]
    d = c * 4
    print("c: ", c)
    print("d: ", d)
    s = [[-1, 1]] * 5
    # s = [-1, 1] * 5
    print("s: ", s)
    s[1].append(7)
    print("s: ", s)

    # Index method
    w = "the quick brown fox jumps over the lazy dog".split()
    print("w: ", w)
    i = w.index('fox')
    print("The index of 'fox' entry is: ", i, w[i])
    # If no index is found it will throw a ValueError
    # i = w.index('cat')
    # print("The index of 'cat' entry is: ", i, w[i])

    # Membership test with: count()
    print("'the' value is: ", w.count("the"))

    # Also test membership with: in, not in
    print(37 in [12,22,37,99])
    print(78 not in [12,22,37,99])

    # Removing elements from list: index and del
    w = "the quick brown fox jumps over the lazy dog".split()
    print(len(w), w)
    del w[2]   # delete using index
    print(len(w), w)
    # remove using: remove()
    w.remove("over")
    print(len(w), w)
    # same as
    del w[w.index('lazy')]
    w[w.index('jumps')] = 'jumped'
    print(len(w), w)

    # Rearranging the list of elements
    g = [1, 11, 21, 1211, 112111]
    print("g:", g)
    g.reverse()  # This is a permanent change.
    print("reverse g: ", g)
    g.reverse()
    print("reverse g again: ", g)

    # Sort method accepts two arguments, key and reverse
    d = [22, 34, 54, 65, 67, 88, 1, 21]
    print("d: ", d)
    d.sort()
    print("d after sort: ", d)
    d.sort()
    d.sort(reverse = True)
    print("d after reverse sort: ", d)

    # Sort by key
    w = "the quick brown fox jumps over the lazy dog".split()
    print(w)
    w.sort(key = len)
    print(w)






if __name__ == '__main__':
    main()
    exit(0)