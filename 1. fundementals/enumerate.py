# Enumerate
# enumerate returns tuples like (0,1) where '0' is the index and '1' is the value
# enumerate takes an optional start property
def fizz_buzz_enumerate(arr):
    '''
    >>> numbers = [45, 22, 14, 65, 97,  72]
    >>> fizz_buzz_enumerate(numbers)
    >>> numbers
    ['fizzbuzz', 22, 14, 'buzz', 97, 'fizz']
    '''
    for i, num in enumerate(arr):
        if num % 3 == 0:
            arr[i] = "fizz"
        if num % 5 == 0:
            arr[i] = "buzz"
        if num % 3 == 0 and num % 5 == 0:
            arr[i] = "fizzbuzz"
    
    # for i, num in enumerate(arr, start=10):