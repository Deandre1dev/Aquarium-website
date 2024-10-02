from .cart import Cart

# Create a context proccessor so our cart can work on all pages.

def cart(requets):
    # Return the default data from our Cart.
    return {'cart': Cart(requets)}