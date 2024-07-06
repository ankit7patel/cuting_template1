from django.shortcuts import render


# Create your views here.


def home(request):
    return render (request, 'home.html')

def shop(request):
    return render(request, 'shop.html')

def blog(request):
    return render(request, 'blog.html')


def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')