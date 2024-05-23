# Arithmetic

# Whole Numbers (Int)
ten = 10

# Decimals (Float)
price = 9.99

# Addition
print(10 + 5)

# Subtraction
print(10 - 5)

# Multiplication
print(10 * 5)

# Dividion
print(10 / 3)
print(10 // 3)
print(10 % 3)

# Exponents
print(10**3)


# Incrementing / Decrememnting
count = 0

count += 15  # count = count + 15
print(count)  # 15

count -= 2  # count = count - 2
print(count)  # 13

count *= 3  # count = count * 3
print(count)  # 39

count /= 2  # count = count / 2
print(count)  # 19.5


# Operator Precenence
# PEMDAS – Parenthesis, Exponents, Multiplication, Division, Addition, Subtraction
problem_one = 10 + 3 * 2  # (3 * 2) + 10 = 6 + 10 = 16
print(problem_one)


# Helpful Functions
number = 2.9

# Rounding
print(round(number))  # 3

# Absolute Value
print(abs(-100))  # 100

# Math module
# https://docs.python.org/3/library/math.html
#
# Add this at the top of the file:  import math
# For specific methods, add: from math import ceil
from math import ceil, floor

print(ceil(number))  # 3
print(floor(number))  # 2
