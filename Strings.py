"""
Strings and Collections

A string is a immutable sequence of Unicode code-points
"""
print ('This is a string')
print ("This is a string too")
print ("I can't do this")

# Concatenation and adjacent Strings

s1 = "First"
s2 = "Second"
print (s1 + " " + s2)

# Multi-line Strings and newlines

s3="""This is 
a multi-line
string"""
print(s3)
s4 = "This is\na multi-line\nstring"
print(s4)

# Python supports Uni-code
# Support for backslash

s5 = "A\\in a String"
print (s5)
s6 = 'this is " wow '
print (s6)


# Raw Strings
raw_string = r'C:\temp'
print (raw_string)

# String as sequence

s = "parrot"
# index notation 0,1,2,3,4,5,6  etc
print("s[4]", s[4], type(s))

# Capitalize the string
print (s, s.capitalize())
