from django import forms

from .models import Product

class ProductForm(forms.ModelForm):
    title       = forms.CharField(label='',
                            widget=forms.TextInput(attrs={"placeholder": "Your title"}))
    email       = forms.EmailField()
    description = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={
                "placeholder": "Your description",
                "class": "new-class-name two",
                "id": "my-id-for-textarea",
                "rows": 20,
                "columns": 120

            }
        )
    )

    price       = forms.DecimalField(initial=199.99)

    class Meta:
        model = Product   # from models.Product
        # this will change the format order in the pages
        fields = [
            'title',
            'email',
            'description',
            'price'
        ]

    #ToDo: 傑に聞く
    def clean_title(self, *args, **kargs):
        title = self.cleaned_data.get("title")
        if not "CFE" in title:
            raise forms.ValidationError("This is not valid title")
        if not "news" in title:
            raise forms.ValidationError("This is not valid title")
        return title

    def clean_email(self, *args, **kargs):
        email = self.cleaned_data.get("email")
        if not email.endswith(".edu"):
            raise forms.ValidationError("This is not valid email")
        return email


class RawProductForm(forms.Form):
    title       = forms.CharField(label='', widget=forms.TextInput(attrs={"placeholder": "Your title"}))
    description = forms.CharField(
                        required=False,
                        widget=forms.Textarea(
                            attrs={
                                "placeholder": "Your description",
                                "class": "new-class-name two",
                                "id": "my-id-for-textarea",
                                "rows": 20,
                                "columns": 120

                            }
                        )
                    )
    price       = forms.DecimalField(initial=199.99)