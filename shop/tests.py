from django.test import TestCase
from .views import product_list, product_detail
from .models import Product


class ViewsShopTestCase(TestCase):
    ''''''

    def setUp(self):
        ''''''
        self.query_product_list = product_list(request='/')
        self.query_product_detail = product_detail(request='3/osoboe/', id=3, slug='osoboe')

    def test_produc_list(self):
        '''product list'''
        self.assertEqual(self.query_product_list, product_list(request='/'))


# Create your tests here.
