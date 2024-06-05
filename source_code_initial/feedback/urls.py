#feedback/urls.py

from django.urls import path, include
from rest_framework import routers
from .api import ProductViewSet

from feedback.views import FeedbackFormView, SuccessView

app_name = "feedback"

#suppously, DefaultRouter() creates the CRUD
router = routers.DefaultRouter()

#urls created with simple CRUDs
router.register(r'products', ProductViewSet, basename='products')

urlpatterns = [
    path("", FeedbackFormView.as_view(), name="feedback"),
    path("success/", SuccessView.as_view(), name="success"),
    
    #this adds the urls created in router for the CRUD
    path('api/', include(router.urls)),
]
