from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView

from feedback.forms import FeedbackForm


class FeedbackFormView(FormView):
    template_name = "feedback/feedback.html"
    form_class = FeedbackForm
    success_url = "/success/"

    def form_valid(self, form):
        # form.send_email()
        # return super().form_valid(form)
        
        try:
            form.send_email()
        except Exception as e:
            # Maneja el error aquí (por ejemplo, registra el error, muestra un mensaje de error, etc.)
            print(f"Error al enviar el correo: {e}")
            # Opcional: Puedes redirigir a una página de error o mostrar un mensaje en la misma página
        return super().form_valid(form)


class SuccessView(TemplateView):
    template_name = "feedback/success.html"
