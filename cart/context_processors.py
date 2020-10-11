from  .cart import Cart


def cart(request):
    '''Context processor for add context in cart'''
    return {'cart': Cart(request)}