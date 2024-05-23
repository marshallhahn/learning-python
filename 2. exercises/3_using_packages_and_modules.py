# Packages work by importing like this:
# import utilities.shipping
#
# And then used like this:
# utilities.shipping.calculate_shipping()

# Or, packages can be imported like this, which is
# more specific and can sometimes be cleaner:
from utilities.shipping import calculate_shipping, calculate_tax

# And then used like this:
calculate_shipping()
calculate_tax()
