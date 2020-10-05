from django.urls import path
from . import views
app_name = 'shop'

urlpatterns = [
    # call views.product_list without additionally parametrs
    path('', views.product_list, name='product_list'),
    # call views.products_list with parametrs category_slug
    path('<slug:category_slug>/', views.product_list,
         name = 'proguct_list_by_category'),
    # call with parametrs id and slug
    path('<int:id>/<slug:slug>/', views.product_detail,
         name='product_detail'),
]