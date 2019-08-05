"""
Getting information from the WEB and working with the contents
http://icarus.cs.weber.edu/-hvalle/hafb/words.txt
Task 1: Count number of words in document
"""

from urllib.request import urlopen


def fetch_words(filename):
    """
    Fetch the words from a file on the WEB
    :return: nothing
    """

    count = 0
    data = []

    with urlopen(filename) as story:
        for line in story:
            words = line.decode('utf-8').split()
            for word in words: # check to see if key already in dict.
                data.append(word)
    return data
               # if word in data:
                #    data[word] += 1
                #else:
                 #   data[word] = 1
                #count += 1
   # for key in sorted(data.keys()):
    #    print (key, data[key])

def print_items(items):
    """
    print elements of the list
    :param items: a collection of objects
    :return: nothing
    """
    for item in items:
        print(item)


def main():
    # file = "c:/windows/default.help.txt"
    file = "http://icarus.cs.weber.edu/~hvalle/hafb/words.txt"
    words = fetch_words(file)
    print_items(words)


if __name__ == "__main__":
    main()
    exit(0)