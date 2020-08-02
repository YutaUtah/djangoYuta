from django import forms

from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product   # from models.Product
        fields = [
            'title',
            'description',
            'price'
        ]