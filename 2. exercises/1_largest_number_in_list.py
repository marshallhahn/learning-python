import random


def generate_random_list_of_numbers(count, min, max):
    rand_list = []
    for i in range(count):
        rand_list.append(random.randint(min, max))
    return rand_list


numbers = generate_random_list_of_numbers(5, -100, 100)
print(numbers)

largest_number = float("-inf")
for n in numbers:
    if n > largest_number:
        largest_number = n

print(largest_number)
