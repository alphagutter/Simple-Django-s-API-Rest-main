from .models import Product
from rest_framework import viewsets, permissions
from .serializers import ProductSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()

    #this allows to everyone to have access to the CRUD made for the RestAPI
    permission_classes = [permissions.AllowAny]
    
    serializer_class = ProductSerializer