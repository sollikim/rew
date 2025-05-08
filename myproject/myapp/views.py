from rest_framework import viewsets
from .models import Product
from .serializers import ProductSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()  # Все продукты
    serializer_class = ProductSerializer  # Используем сериализатор для модели Product