#django_celery/urls.py

from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),

    #recordatorio: feedback.urls hace referencia a la carpeta feedback que tiene el archivo urls.py
    path("", include("feedback.urls")),
]
