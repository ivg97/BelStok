from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from shop.models import Product
from .cart import Cart
from .forms import CartAddProductForm


@require_POST
def cart_add(request, product_id):
    '''Handler add product in cart'''
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product,
                 quantity=cd['quantity'],
                 update_quantity=cd['update'])
        print('-'*70, '\n3 - detail.html - cart_add: ', product.name, '\n','-'* 70)
    return redirect('cart:cart_detail')


def cart_remove(request, product_id):
    '''Handler delete product from cart'''
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('cart:cart_detail')


def cart_detail(request):
    '''Handler page for page list product, add in cart'''
    cart = Cart(request)
    return render(request, 'cart/detail.html',
                  {'cart': cart})

# Create your views here.
