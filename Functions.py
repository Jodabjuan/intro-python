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

def main():
    """
    Test Function
    :return:nothing
    """
    #call function
    print(__name__)
    even_or_odd(89)
    even_or_odd(44)

if __name__ == "__main__":
    main()
    exit(0)

# load it in the console
#import Functions (gets both even_or_odd(number) and main()
#from Functions import even_or_odd(number) as <name> to load only one