from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def home_view(request, *args, **kwargs):
    return render(request, "home.html", {})

def contact_view(request, *args, **kwargs):
    return HttpResponse("<h1>contact</h1>")

def about_view(request, *args, **kwargs):
    my_context = {
        "my_text": "this is about my pages",
        "my_number": 22,
        "my_list" : [5,15,25]
    }
    return render(request, "about.html", my_context)