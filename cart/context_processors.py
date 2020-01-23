from .cart import Cart

#a function that receives the request object and returns 
#a dictionary of objects available to all the templates rendered
def cart(request):
    return {'cart': Cart(request)}
