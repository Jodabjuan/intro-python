"""
Getting information from the WEB and working with the contents
http://icarus.cs.weber.edu/-hvalle/hafb/words.txt

Task 1: Count number of words in document
"""

# this is a very large library - getting only one function (import)
from urllib.request import urlopen


def fetch_words(filename):
    """
    Count words in url file
    :param filename: url to file
    :return: a list of the items
    """

    count = 0
    data = []

    with urlopen(filename) as story:
        for line in story:
            words = line.decode('utf-8').split() # .split seperates the pieces using the spaces as delimiter.
            for word in words: # check to see if key already in dict.
                data.append(word)
    return data


def print_items(items):
    """
    print elements of the list
    :param items: a collection of objects
    :return: nothing
    """
    for item in items:
        print(item)


def main():
    """
    Test function for words Library
    :return: nothing
    """
    # file = "c:/windows/default.help.txt"
    file = "http://icarus.cs.weber.edu/~hvalle/hafb/words.txt"
    words = fetch_words(file)
    print_items(words)


if __name__ == "__main__":
    main()
    exit(0)