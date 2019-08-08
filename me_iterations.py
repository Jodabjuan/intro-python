"""
When working with iterators, generators, etc
look at the documentation for the itertools module
"""
from itertools import islice, count
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


if __name__ == '__main__':
    main()
    exit(0)