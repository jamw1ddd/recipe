from django.core.management.base import BaseCommand
from django.core.mail import send_mail


class Command(BaseCommand):
    help = 'Send Email'

    def handle(self, *args, **options):
        send_mail('Test mail', 'this is a test email111ewrwerwerwerwerwerwe',
                  'jamw1ddd2002@gmail.com', ['jamw1ddd2002@gmail.com'], fail_silently=False)
        self.stdout.write(self.style.SUCCESS('Email sent successfully!'))
