# Logical Operators
#
# == – Equals
# === - Equals (Strict)
# != – Does Not Equal
# > - Greater than
# < - Less than
# >= - Greater than or equal to
# <= - Less than or equal to

# number = 100
# if number > 99:
#     print("Number is greater than 99")
# else:
#     print("Number is not greater than 99")


name = input("What is your name? ")
name_length = len(name)

if name_length >= 3 and name_length <= 50:
    print("Name looks great")

if name_length < 3:
    print("Name must be at least 3 characters long")

if name_length > 50:
    print("Name can be a maximum of 50 characters long")
