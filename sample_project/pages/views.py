from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home_view(request,*args, **kwargs):
    # return HttpResponse("<h1>Hello world </h1>")
    print(*args, ** kwargs)
    print(request)
    return render(request, "home.html", {})

def contact_view(request,*args, **kwargs):
    return render(request, "contact.html", {})

def about_view(request,*args, **kwargs):
    my_context = {
        "title": "contact details",
        "contact_exist": True,
        "my_contact": 123456789,
        "my_list": [123456789, 234567890, 345678921, "Abc"],
        "my_html": "<h1>Hello World</h1>"

    }
    return render(request, "about.html", my_context)

def social_view(request,*args, **kwargs):
    return HttpResponse("<h1>Sopcial page</h1>")