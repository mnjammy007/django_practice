from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("about", views.about, name="about"),
    path("contact", views.contact, name="contact"),
    path("send_email", views.send_email, name="send_email"),
    path("send_attachment_email", views.send_attachment_email, name="send_attachment_email"),
]
