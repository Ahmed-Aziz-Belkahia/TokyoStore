from django.urls import path
from blog import views

app_name = "blog"

urlpatterns = [
    path("blog-full-width/", views.blog_full_width, name="blog_full_width"),
    path("blog-v1/", views.blog_v1, name="blog_v1"),
    path("blog-v2/", views.blog_v2, name="blog_v2"),
    path("blog-v3/", views.blog_v3, name="blog_v3"),
    path("single-blog-post/", views.single_blog_post, name="single_blog_post"),
]