# Strings

# Basic string
print("This is a string")


# Concat two strings
print("Number 1, " + "Number 2")


# Interpolation
print("My name is %s and I like %s" % ("Marshall", "Coffee"))
print("My name is {0} and I like {1}".format("Marshall", "Coffee"))
print(
    "My name is {name} and I like {favorite_beverage}".format(
        name="Marshall", favorite_beverage="Coffee"
    )
)


# f-string
print(f"What is 2 * 10? The answer is: {2 * 10}")


# Iterate and print values with f-string
numbers = [1, 2, 3, 4, 5]
for _, num in enumerate(numbers):
    print(f"Number {num}")


# Multiple line strings
multi_line_string = """
This is a multi-line string.
It spans multiple lines.
"""
print(multi_line_string)


# Single quotes vs double quotes
single_quote = 'This is a single quote string, it can use "double quotes" inside.'
double_quote = "This is a double quote string, it can use 'single quotes' inside."
print(single_quote, double_quote)


# String chars can be accessed by index
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# Defaults are 0 and -1
print(alphabet[:])  # ABCDEFGHIJKLMNOPQRSTUVWXYZ

print("First letter: " + alphabet[0])  # A
print("Last letter: " + alphabet[-1])  # Z
print("Letters 1 (A) through 10 (J): " + alphabet[0:10])  # ABCDEFGHIJ
print("Letters 9 (J) through 16 (P): " + alphabet[9:16])  # KLMNOP
print("Letters 15 (P) through 26 (Z): " + alphabet[15:])  # PQRSTUVWXYZ
print("Letters B through Y: " + alphabet[1:-1])  # BCDEFGHIJKLMNOPQRSTUVWXYZ


# Length of a string
print(len(alphabet))

# String methods
print(alphabet.upper())
print(alphabet.lower())
print(alphabet.title())
print(alphabet.capitalize())
print(alphabet.find("P"))
print(alphabet.replace("A", "a"))
print(alphabet.strip("ABC"))

# Search for char in string
print("D" in alphabet)  # True
print("1" in alphabet)  # False
