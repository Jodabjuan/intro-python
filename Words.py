"""
Getting information from the WEB and working with the contents
http://icarus.cs.weber.edu/-hvalle/hafb/words.txt
Task 1: Count number of words in document
"""

from urllib.request import urlopen
file = "http://icarus.cs.weber.edu/~hvalle/hafb/words.txt"
count = 0
data = {}

with urlopen(file) as story:
    for line in story:
        words = line.decode('utf-8').split()
        for word in words: # check to see if key already in dict.
            if word in data:
                data[word] += 1
            else:
                data[word] = 1
            count += 1
print("Total number of words: ", count)
print("Total data: ", data)