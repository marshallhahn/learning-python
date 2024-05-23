# Type Conversion
#
# str() - Convert to string
# int() – Convert to int
# float() – Convert to float
# bool() – Convert to boolean

# String to Int
birth_year = input("What is your birth year? ")
current_year = 2024
age_estimate = current_year - int(birth_year)
print(age_estimate)

# Weight – lbs to kg
weight_lbs = input("Weight (lbs): ")
weight_kg = float(weight_lbs) * 0.45
print(weight_kg)
