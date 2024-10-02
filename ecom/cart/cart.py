class Cart():
    def __init__(self, request):
        self.session = request.session

        # Get the users curent session key if it exists.
        cart = self.session.get('session_key')

        # if the user is new create a session key.
        if 'session_key' not in request.session:
            cart = self.session['session key'] = {}

        # Make sure cart is available on all the web pages.
        self.cart = cart    
