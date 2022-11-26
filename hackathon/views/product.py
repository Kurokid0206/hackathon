from rest_framework.viewsets import ModelViewSet

from hackathon.models import Product
from hackathon.serializers.product import ProductSerializer


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
