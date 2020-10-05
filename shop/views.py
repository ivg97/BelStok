from django.shortcuts import render, get_object_or_404
from .models import Category, Product


def product_list(request, category_slug=None):
    '''Handler create page is list products and filter by categories'''
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(avialable=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request, 'shop/product/list.html',
                  {'category':category,
                   'categories': categories,
                   'progucts':products,
                   })

def product_detail(request, id, slug):
    '''Hander display page every product'''
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    return render(request, 'shop/product/detail.html',
                  {'proguct': product})


# Create your views here.
