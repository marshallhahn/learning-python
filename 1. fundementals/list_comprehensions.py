# List Comprehensions
numbers = [1, 2, -5, 4]

def square(x):
    '''
    Takes a value and multiplies it by itself to get the square
    >>> square(2)
    4
    >>> square(5)
    25
    '''
    return x * x

def is_odd(x):
    '''
    Takes a value and checks if there is a remainder after dividing by 2.
    If there is a remainder, the input is odd, otherwise it is even.
    >>> is_odd(2)
    False
    >>> is_odd(3)
    True
    '''
    return x % 2 == 1

# print(list(map(square, numbers)))

# Loop
# result = []
# for num in numbers:
#     result.append(square(num))
# print(result)

# Comprehension
# print(
#     [square(num) for num in numbers]
# )


# list(filter(is_odd, numbers))
# print(
#     [num for num in numbers if is_odd(num)]
# )



# grid = [[0, 0, 0],
#         [0, 0, 0],
#         [0, 0, 0]]

# num_rows = 3
# num_columns = 4

# grid = []
# for _ in range(num_rows):
#     current_row = []
#     for _ in range(num_columns):
#         current_row.append(0)
#     grid.append(current_row)
# print(grid)

# grid = [[0 for _ in range(num_columns)] for _ in range(num_rows)]
# print(grid)