numbers = [1, -5, 75, 30, -100]

# max
max_num = max(numbers)
print(max_num)

# max with lambda
max_squared = max(numbers, key=lambda x: x * x)
print(max_squared)

# min with lambda
min_squared = min(numbers, key=lambda x: x * x)
print(min_squared)



# any
# returns true if any values in a list are True, and False if none are true
any_numbers = any(numbers)
print(any_numbers)

any([True, False]) # True
any([False, False]) # False

any([(lambda x: x % 2 == 1)(num) for num in numbers])



# all
# similar to any, but each item needs to be true, otherwise it will return False
all([(lambda x: x % 2 == 1)(num) for num in numbers])