"""
List Comprehensions:
Readable, expressive, and effective
"""
from math import factorial, sqrt
from pprint import pprint as pp


def is_prime(num):
    """
    Is the number (num) prime
    :param num: number to test
    :return: True for prime # or False for not prime #
    """
    if num < 2:
        return False
    for i in range(2, int(sqrt(num))+1):
        if num % i == 0:
            return False

    return True


def main():
    """
    Test function
    :return:
    """
    words = "Today I am very happy to learn about list comprehensions".split()
    # print(words)
    data = []  # empty list
    for word in words:
        # do some sort of analysis
        data.append(word)

    # "Filter" data
    print(data)

    # Task is to find the length of the first 20 factorial numbers
    # how many digits for 1st, for 2nd, for 3rd ...
    numdig = []
    for x in range(20):
        numdig.append(len(str(factorial(x))))

    pp(numdig)

    # Use a list Comprehension: []
    info2 = [len(str(factorial(x)))for x in range(20)]  # loop and actions in one line (not 3 line above)
    pp(info2)

    # Set Comprehensions: {}
    info3 = {len(str(factorial(x)))for x in range(20)}  # for sets (removes dups)
    pp(info3)

    # Dictionary Comprehensions: {}
    nba_teams = {'jazz':'SLC', 'warriors':'OAKLAND', 'lakers':"LA", 'clippers':"LA"} #key must be unique
    pp(nba_teams)
    teams_nba = {city:mascot for mascot, city in nba_teams.items()}
    pp(teams_nba)

    # Filter predicates
    primes = [x for x in range(10001) if is_prime(x)]
    print("Qty of primes: ", len(primes), " - ", primes)







if __name__ == '__main__':
    main()
    exit(0)