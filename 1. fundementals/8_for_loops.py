# For Loops

for i in [1, 2, 3, 4, 5]:
    print(i)

for val in ["M", "A", "R", "S", "H"]:
    print(val)

# using range
for i in range(10):
    print(i)

# using enumerate
for index, value in enumerate([1, 2, 3, 4, 5]):
    print((index, value * 2))


# Nested Loop
for x in range(10):
    print(f"\n{x} Coordinates:")
    for y in range(4):
        print(f"({x}, {y + 1})")

# 0 Coordinates:
# (0, 1)
# (0, 2)
# (0, 3)
# (0, 4)

# 1 Coordinates:
# (1, 1)
# (1, 2)
# (1, 3)
# (1, 4)

# 2 Coordinates:
# (2, 1)
# (2, 2)
# (2, 3)
# (2, 4)

# 3 Coordinates:
# (3, 1)
# (3, 2)
# (3, 3)
# (3, 4)


for value in [5, 2, 5, 2, 2]:
    output = ""
    for i in range(value):
        output += "x"
    print(output)
