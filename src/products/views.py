from django.shortcuts import render, get_object_or_404, redirect

from .forms import ProductForm, RawProductForm
from .models import Product
# Create your views here.




# def product_create_view(request):
#     my_form = RawProductForm(request.GET)
#     if request.method == "POST":
#         my_form = RawProductForm(request.POST)
#         if my_form.is_valid():
#             print(my_form.cleaned_data)
#             Product.objects.create(**my_form.cleaned_data) # create an object no need to use save()
#         else:
#             print(my_form.errors)
#     context = {
#         "form": my_form
#     }
#
#     return render(request, "products/product_create.html", context)



# def product_create_view(request):
#
#     if request.method == 'POST':
#         my_new_title = request.POST.get('title')
#         # Product.objects.create(title=my_new_title)
#
#     context = {}
#     return render(request, "products/product_create.html", context)

def product_create_view(request): #django usage
    # initial data is passed on through context >> dictionalized by "form"
    initial_data = {
        'title': 'this is an awesome title'
    }
    obj = Product.objects.get(id=1)
    form = RawProductForm(request.POST or None, initial=initial_data)

    if form.is_valid():
        form.save()
        form = ProductForm(request.POST or None)
        form = ProductForm()

    context = {
        'form': form
    }
    return render(request, "products/product_create.html", context)



def product_detail_view(request):
    obj = Product.objects.get(id=1)
    context = {
        'title': obj.title,
        'description': obj.description
    }

    # better to use the one below: (change the variables in detail.html)
    context = {
        'object': obj
    }
    return render(request, "products/product_detail.html", context)


def dynamic_lookup_view(request, my_id):
    obj = Product.objects.get(id=my_id)
    context = {
        'object': obj
    }
    return render(request, "products/product_detail.html", context)

def product_delete_view(request, id):
    obj = get_object_or_404(Product, id=id)
    # POST Request
    if request.method == "POST":
        obj.delete()
        return redirect('../../')
    context = {
        "object": obj
    }
    return render(request, "products/product_delete.html", context)

def product_list_view(request):
    queryset = Product.objects.all()
    context = {
        "object_list": queryset
    }
    return render(request, "products/product_list.html", context)