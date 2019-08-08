"""
When working with iterators, generators, etc
look at the documentation for the itertools module
"""
from itertools import islice, count, chain
from list_comprehensions import is_prime


def main():
    """
    Test function
    :return:
    """
    thousand_primes = islice((x for x in count() if is_prime(x)), 1000)
    print(thousand_primes, type(thousand_primes))
    print("List of frist 1K prime numbers: ", list(thousand_primes))
    # Note: if you need to use the object again, you need to re-generate it.
    thousand_primes = islice((x for x in count() if is_prime(x)), 1000)
    print("Sum of frist 1K prime numbers: ", sum(thousand_primes))
    # Other built-ins use with itertools: any (like "or"), all (like "and")
    print(any([False, False, True]))
    print(all([False, False, True]))
    print("Are there prime numbers between 1328 and 1362: ", any(is_prime(x) for x in range(1328, 1362)))
    # Check if all names are in "Title" format
    names = ["London", "New York", "ogden"]
    print(all(name == name.title() for name in names))
    # Another built-in: zip()
    sunday = [2, 2, 5, 7, 9, 10, 9, 6, 4, 4]
    monday = [12, 14, 14, 15, 15, 16, 15, 13, 10, 9]
    tuesday = [13, 14, 15, 15, 16, 17, 16, 16, 12, 12]
    wednesday = [12, 12]
    for item in zip(monday, tuesday):
        print(item)
    for mon, tue in zip(monday, tuesday):  #unpacked the tuple
        print("Avg: ", (mon + tue)/2)
    # Calculate the min, max and avg of all points
    for temp in zip(sunday, monday, tuesday):
        print("Min={:7.3f}   Max={:7.3f}   Avg={:7.3f}".format(
            min(temp), max(temp), sum(temp)/len(temp)))
    # chaining
    all_temps = chain(sunday, monday, tuesday)
    print("All temps > 0: ", all(t > 0 for t in all_temps))


if __name__ == '__main__':
    main()
    exit(0)