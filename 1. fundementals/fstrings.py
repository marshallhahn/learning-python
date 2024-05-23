# Formatted String Literals
# 
# Available in Python 3.6+
# 
# NOTE: It is dangerous to use f-string with user input
# This is because f-strings let you evaluate arbitrary 
# Python expressions (i.e. executing system commands, file removal)

name = 'Marshall'
favorite_beverage = 'Coffee'
years_of_experience = 3

# F string
print(f"My name is {name}")
# Inline number calculation
print(f"My name is {name} and I have {years_of_experience + 1} yrs of experience")


# Helpful in classes
class Human(object):
    def __init__(self, name, years_of_experience) -> None:
        self.name = name
        self.years_of_experience = years_of_experience
    def __repr__(self) -> str:
        return f"""
            My name is {self.name}.
            I have {self.years_of_experience + 1} yrs of experience.
        """
print(Human(name, years_of_experience))


# Other ways to do this
# If using python version below 3.6
print("My name is %s and I like %s" % (name, favorite_beverage))
print("My name is {0} and I like {1}".format(name, favorite_beverage))
print("My name is {name} and I like {favorite_beverage}".format(name=name, favorite_beverage=favorite_beverage))