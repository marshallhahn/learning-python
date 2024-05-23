# Doctest
# The doctest module searches for pieces of text that look like interactive Python sessions, 
# and then executes those sessions to verify that they work exactly as shown.

# To run doctests execute the following:
# python3 -m doctest <file>

def plus_one(n):
    '''Returns the input number plus one

    >>> plus_one(1)
    2
    >>> plus_one(99)
    100
    >>> plus_one("A")
    Traceback (most recent call last):
      ...
    TypeError: can only concatenate str (not "int") to str
    '''
    
    return n + 1