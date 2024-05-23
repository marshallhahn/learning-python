def check_temperature(temperature):
    """Return a recommendation based on the temperature in celcius.

    >>> check_temperature(79)
    It is comfortable. Wear layers.
    >>> check_temperature(80)
    It is HOT. Wear sunscreen!
    >>> check_temperature(65)
    It is COLD. Wear a coat.
    """

    try:
        val = float(temperature)
        if val > 79:
            print("It is HOT. Wear sunscreen!")
        if val > 65 and val <= 79:
            print("It is comfortable. Wear layers.")
        if val <= 65:
            print("It is COLD. Wear a coat.")
    except ValueError:
        print("Temperature must be a float.")


# temperature = input("What is the temperature in celcius? ")
# check_temperature(temperature)


def check_credit(home_price, credit_score):
    """Return down payment amount based on home price and credit score

    >>> check_credit(1_000_000, 650)
    200000
    >>> check_credit(1_000_000, 800)
    100000
    """
    if credit_score > 700:
        return print(int(home_price * 0.10))

    print(int(home_price * 0.20))


score = input("What is your credit score? ")
check_credit(1_000_000, int(score))
