#feedback/tasks.py

from time import sleep
from django.core.mail import send_mail
from celery import shared_task


@shared_task()
def send_feedback_email_task(email_address, message):
    """Send an email when the feedback has been subtmitted"""

    sleep(5)  # Simulate expensive operation(s) that freeze Django

    send_mail("Tu respuesta: ",
              f"\t '{message}'\n\n fue enviada",
              "support@example.com",
              [email_address],
              fail_silently=False)
    