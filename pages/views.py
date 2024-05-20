from django.shortcuts import render

# Create your views here.


def page_404(request, *args, **kwargs):
    return render(request, "home/404.html", {})

def about(request, *args, **kwargs):
    return render(request, "home/about.html", {})

def home_v2(request, *args, **kwargs):
    return render(request, "home/home-v2.html", {})

def store_directory(request, *args, **kwargs):
    return render(request, "home/store-directory.html", {})

def terms_and_conditions(request, *args, **kwargs):
    return render(request, "home/terms-and-conditions.html", {})