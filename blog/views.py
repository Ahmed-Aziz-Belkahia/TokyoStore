from django.shortcuts import render

# Create your views here.

# Blog Views
def blog_full_width(request, *args, **kwargs):
    return render(request, "blog/blog-full-width.html", {})

def blog_v1(request, *args, **kwargs):
    return render(request, "blog/blog-v1.html", {})

def blog_v2(request, *args, **kwargs):
    return render(request, "blog/blog-v2.html", {})

def blog_v3(request, *args, **kwargs):
    return render(request, "blog/blog-v3.html", {})

def single_blog_post(request, *args, **kwargs):
    return render(request, "blog/single-blog-post.html", {})