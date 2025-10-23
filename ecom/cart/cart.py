class Cart:
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get('cart')   # use a consistent key name

        if not cart:
            # if the user is new, create an empty cart
            cart = self.session['cart'] = {}

        self.cart = cart

    def add(self, product):
        product_id = str(product.id)

        # If product already in cart, you could increase quantity
        if product_id in self.cart:
            # Example: track quantity
            self.cart[product_id]['quantity'] += 1
        else:
            self.cart[product_id] = {
                'price': str(product.price),
                'quantity': 1
            }

        # Mark the session as modified so Django saves it
        self.session.modified = True

    def __len__(self):
        """
        Return the total number of items in the cart (sum of quantities).
        """
        return sum(item['quantity'] for item in self.cart.values())
