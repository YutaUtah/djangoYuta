from django.contrib import admin
from django.urls import path

from pages.views import home_view, contact_view, about_view
from products.views import (product_detail_view,
                            product_create_view,
                            dynamic_lookup_view,
                            product_delete_view,
                            product_list_view)



urlpatterns = [
    path('contact/', contact_view, name='home'),
    # path('product/', product_detail_view, name='home'),
    path('products/<int:my_id>/', dynamic_lookup_view, name='product-detail'),
    path('products/', product_list_view, name='product'),
    path('create/', product_create_view, name='create'),
    path('products/<int:id>/delete/', product_delete_view, name='product-delete'),
]
