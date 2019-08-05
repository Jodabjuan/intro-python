"""
Getting information from the WEB and working with the contents
http://icarus.cs.weber.edu/-hvalle/hafb/words.txt
Task 1: Count number of words in document
"""

from urllib.request import urlopen
file = "http://icarus.cs.weber.edu/~hvalle/hafb/words.txt"

with urlopen(file) as story:
    for line in story:
        
        print(line)