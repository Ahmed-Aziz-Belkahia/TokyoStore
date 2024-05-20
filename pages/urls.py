from django.urls import path
from pages import views

app_name = "pages"

urlpatterns = [
    path("", views.home_v2, name="home_v2"),
    path("404/", views.page_404, name="404"),
    path("about/", views.about, name="about"),
    path("store-directory/", views.store_directory, name="store_directory"),
    path("terms-and-conditions/", views.terms_and_conditions, name="terms_and_conditions"),
]