# Logical Operators
#
# AND – condition and condition
# OR - condition or condition
# NOT - not condition

# AND
subscribed = True
accepted_terms = True
if subscribed and accepted_terms:
    print("Subscriber has accepted terms.")

# OR
subscribed = True
trial = False
if subscribed or trial:
    print("User has the feature because they are subscribed or have the trial.")

# NOT
subscribed = True
access_denied = False
if subscribed and not access_denied:
    print("Subscriber is allowed to access the record.")
