from django.contrib import admin
# "." means relative import
from .models import Product

# Register your models here.
admin.site.register(Product)
