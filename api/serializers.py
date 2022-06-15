from rest_framework.serializers import ModelSerializer
from .models import Product
from .models import User


class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'        