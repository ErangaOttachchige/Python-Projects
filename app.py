# ecommerce.shipping     # We have to prefix it with the name of its package
from ecommerce.shipping import calc_shipping

# To import the entire module,
from ecommerce import shipping   # From "ecommerce" package import "shipping" module

# now to access any of the functions or classes in this module
# ecommerce.shipping.calc_shipping()
calc_shipping()
calc_shipping()
calc_shipping()

shipping.calc_shipping()