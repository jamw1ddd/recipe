from celery import shared_task

from django.core.mail import send_mail


@shared_task
def send_email():
    send_mail('Test mail', 'this is a test email', 'jamw1ddd2002@gmail.com', ['jamw1ddd2002@gmail.com'],
              fail_silently=False)
    return 1
