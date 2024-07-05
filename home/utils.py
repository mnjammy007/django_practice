from home.models import Student
import time
from django.core.mail import send_mail, EmailMessage
from django.conf import settings

def run_this_fun():
    print("Nasir here")
    time.sleep(1)
    print("jamal here")

def send_email_to_client(subject, message, email):
    send_mail(
        subject=subject,
        message=message,
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[email],
        fail_silently=False,
    )

def send_email_with_attachment(subject, message, email, attachment):
    mail = EmailMessage(
        subject=subject,
        body=message,
        from_email=settings.EMAIL_HOST_USER,
        to=[email]
    )
    mail.attach_file(attachment)
    mail.send()