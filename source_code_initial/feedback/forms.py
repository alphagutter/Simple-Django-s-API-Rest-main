from time import sleep

from django import forms

#we do not use this anymore because we use celery
#from django.core.mail import send_mail

#task added to pass the responsability to celery
from feedback.tasks import send_feedback_email_task



class FeedbackForm(forms.Form):
    email = forms.EmailField(label="Email Address")
    message = forms.CharField(
        label="Message", widget=forms.Textarea(attrs={"rows": 5})
    )

    def send_email(self):
        # """Sends an email when the feedback form has been submitted."""
        # sleep(1)  # Simulate expensive operation that freezes Django
        # send_mail(
        #     "Your Feedback",
        #     f"\t{self.cleaned_data['message']}\n\nThank you!",
        #     "support@example.com",
        #     [self.cleaned_data["email"]],
        #     fail_silently=False,
        # )

        #cleans the data from send_feedback_email_task
        send_feedback_email_task.delay(
            self.cleaned_data["email"], self.cleaned_data["message"]
        )


