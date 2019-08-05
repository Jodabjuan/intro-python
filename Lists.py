"""
Learn about Lists
Unlike strings, lists are mutable
You can update, and append elements to it
"""

# use [] for lists.
l = [1,2,3]
print("List ", l, type(l))


# A list of objects (Any type)
a = ["apple", "orange", "pear"]
#Access by index notation
# Replace an element
a[0] = "tomatoes"
a[1] = 3.445
print(a, a[0], type(a[1]), type(a[0]))
names = []
counter = 0
while counter < 3:
    name = input("Enter a Name")
    names.append(name)
    counter = counter + 1

print(names)



