from django.shortcuts import render, get_object_or_404
from . cart import Cart
from store.models import Product
from django.http import JsonResponse

# Create your views here.
def cart_summary(request):
    return render(request, "cart_summary.html", {})

def cart_add(request):
    # Get the cart
    cart = Cart(request)
    # Test for POST
    if request.POST.get('action') == 'post':
        # Get information
        product_id = int(request.POST.get('product_id'))

        # Lookup product in the DB
        product = get_object_or_404(Product, id=product_id)

        # Save to a session
        cart.add(product=product)

        # Get Cart quantity.
        cart_quantity = cart.__len__()

        # Return a json response to send back data to the webpage.
        #response = JsonResponse({'Product Name': product.name})
        
        response = JsonResponse({'qty': cart_quantity})
        # Return the response
        return response

def cart_delete(request):
    #Need to add functionality
    pass

def cart_update(request):
    #Need to add functionality#
    pass