from django.urls import path
from help_center import views

app_name = "help_center"

urlpatterns = [
    path("contact-v1/", views.contact_v1, name="contact_v1"),
    path("contact-v2/", views.contact_v2, name="contact_v2"),
    path("faq/", views.faq, name="faq"),
]
