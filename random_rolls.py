"""
Simulate 6000 rolls of a die (1-6)
"""
import random
import statistics


def roll_die(num):
    '''
    Random roll of a die
    :param num: number of rolls
    :return: a list of frequencies
    Index 0 maps 1s
    Index 1 maps 2s
    '''

    freq = [0] * 6  # initial val to 0
    for roll in range(10):
        # print(random.randrange(1, 7))
        n = random.randrange(1, 7)
        print(n)
        freq[n -1] += 1
    return freq




def main():
    """
    Test function
    :return:
    """
    num = int(input("How many times to roll?"))
    l = roll_die(num)
    for roll, total in enumerate(l):
        print("Total rolls of {} = {}".format(roll + 1, total))



if __name__ == '__main__':
    main()
    exit(0)