from django.shortcuts import render

# Create your views here.
def contact_v1(request, *args, **kwargs):
    return render(request, "home/contact-v1.html", {})

def contact_v2(request, *args, **kwargs):
    return render(request, "home/contact-v2.html", {})

def faq(request, *args, **kwargs):
    return render(request, "home/faq.html", {})