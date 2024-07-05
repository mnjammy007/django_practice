import random
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.shortcuts import render
from .utils import send_email_to_client, send_email_with_attachment
from django.conf import settings
from .models import Car


def send_email(request):
    subject = "Django Test"
    message = "Hello from Django"
    email = "mnjamal0106@gmail.com"
    send_email_to_client(subject, message, email)
    return redirect("/home")


def send_attachment_email(request):
    subject = "Django Attachment Test"
    message = "Hello from Django. Please find the attachment below."
    email = "mnjamal0106@gmail.com"
    attachment = f"{settings.BASE_DIR}/public/media/recipe/Chicken_Stew.jpeg"
    send_email_with_attachment(subject, message, email, attachment)
    return redirect("/home")


def home(request):

    Car.objects.create(car_name=f"Toyota{random.randint(1, 100)}")

    my_friends = [
        {"name": "Shamim", "age": 29},
        {"name": "Shahid", "age": 30},
        {"name": "Irfan", "age": 27},
        {"name": "Monu", "age": 28},
        {"name": "Nasir", "age": 29},
    ]
    # return HttpResponse("<h1>I am a Django server</h1>")
    return render(
        request, "home.html", context={"my_friends": my_friends, "page": "Home"}
    )


def about(request):
    return render(request, "about.html", {"page": "About"})


def contact(request):
    return render(request, "contact.html", {"page": "Contact"})
