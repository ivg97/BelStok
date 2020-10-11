from decimal import Decimal
from django.conf import settings
from shop.models import Product

class Cart(object):
    ''' Class with respond without work cart with product'''

    def __init__(self, request):
        '''Inizialisation object cart'''
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        # print('-#-#'*5,'\n', cart, '\n', '-#-end'*5)
        if not cart:
            # Save in session empty cart
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def __iter__(self):
        '''Go cart and get objects Product'''
        product_ids = self.cart.keys()
        # Get objects model Product and transfer to them in cart
        products = Product.objects.filter(id__in=product_ids)
        cart = self.cart.copy()
        for product in products:
            cart[str(product.id)]['product'] = product

        for item in cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item

    def __len__(self):
        '''Return quantity product in cart'''
        return sum(item['quantity'] for item in self.cart.values())


    def add(self, product, quantity=1, update_quantity=False):
        '''Add product in cart or update cart'''
        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = {'quantity': 0,
                                     'price': str(product.price)}
        if update_quantity:
            self.cart[product_id]['quantity'] = quantity
        else:
            self.cart[product_id]['quantity'] += quantity
        self.save()

    def save(self):
        '''Response without change cart'''
        self.session.modified = True

    def remove(self, product):
        '''Done delete product from cart and save new data session'''
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def get_total_price(self):
        '''return sum price product by cart'''
        return sum(Decimal(item['price']) * item['quantity']
                   for item in self.cart.values()
                   )

    def clear(self):
        '''Clear cart'''
        del self.session[settings.CART_SESSION_ID]
        self.save()