"""
Learn Dictionaries
Dict. maps keys to values.

In some languages are known as associative arrays, or hashes, or maps

Create them using { } containing a key-value pair.
Retreive them by [key value]
"""


d = {'alice':'801-123-4567',
     'pedro':'435-594-2541',
     'john': '215-564-6584'}
print(d, type(d))
print(d['john'])


# Add members to the Dictionary, of names-> grades
roster = {}

counter = 0
while counter < 3:
    name = input("Enter a Name")
    grade = input("Enter the Grade.")
    roster[name] = grade
    counter += 1

print(roster)
