# Range
def fizz_buzz(arr):
    '''
    Given a list of integers:
    1. Replace all integers that are evenly divisible by 3 with "fizz"
    2. Replace all integers divisible by 5 with "buzz"
    3. Replace all integers divisible by both 3 and 5 with "fizzbuzz"

    >>> numbers = [45, 22, 14, 65, 97,  72]
    >>> fizz_buzz(numbers)
    >>> numbers
    ['fizzbuzz', 22, 14, 'buzz', 97, 'fizz']
    '''
    for i in range(len(arr)):
        num = arr[i]
        if num % 3 == 0:
            arr[i] = "fizz"
        if num % 5 == 0:
            arr[i] = "buzz"
        if num % 3 == 0 and num % 5 == 0:
            arr[i] = "fizzbuzz"