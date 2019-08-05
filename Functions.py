"""
Learn about functions/definitions
Use the keyword: def <name>():
"""


def even_or_odd(number):
    """
    Find if number is even or odd
    print "even" on even numbers
          "odd" on odd numbers
    :param number: input number
    """
    if number %2 == 0:
        print ("Even")
    else:
        print ("Odd")


#call function
even_or_odd(89)
even_or_odd(44)