# use print
#  print("This is an example: ", variable)

# use breakpoint
#  breakpoint()
#
# breakpoint only available in Python 3.7+
# older versions, import pdb
# import pdb;pdb.set_trace()


def maximum(lst):
    """This will return the highest number in an array
    >>> maximum([-1, 0, 1, 2, 3])
    3
    >>> maximum([-100, -50, -1])
    -1
    >>> maximum([1, -100, 300, 50])
    300
    """
    max_num = float("-inf")
    for num in lst:
        if num > max_num:
            max_num = num

    return max_num


print(maximum([-100, -150, -200, -300]))
