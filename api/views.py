from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.serializers import Serializer
from .models import Product
from .models import User
from .serializers import ProductSerializer
from .serializers import UserSerializer
from django.contrib.auth.hashers import make_password, check_password

# Create your views here.
@api_view(['GET'])
def getRoutes(request):
    routes = [
        {
            'Endpoint': '/products/',
            'method': 'GET',
            'body': None,
            'description': 'Returns an array of products'
        },
        {
            'Endpoint': '/products/id',
            'method': 'GET',
            'body': None,
            'description': 'Returns a single product object'
        },
        {
            'Endpoint': '/products/category/',
            'method': 'GET',
            'body': {'body': ""},
            'description': 'Returns an array of products based on category'
        },
        {
            'Endpoint': '/notes/id/update/',
            'method': 'PUT',
            'body': {'body': ""},
            'description': 'Creates an existing product with data sent in post request'
        },
        {
            'Endpoint': '/notes/id/delete/',
            'method': 'DELETE',
            'body': None,
            'description': 'Deletes and exiting product'
        }
    ]
    return Response(routes)


@api_view(['GET'])
def getProducts(request):  
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getProduct(request, pk):
    product = Product.objects.get(id=pk)
    serializer = ProductSerializer(product, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def createProduct(request):
    data = request.data
    product = Product.objects.create(
       title= data['title'],
       desc= data['desc'],
       img= data['img'],
       category= data['category'],
       color= data['color'],
       price= data['price'],
       size= data['size']
    )
    serializer = ProductSerializer(product, many=False)
    return Response(serializer.data)

@api_view(['GET'])
def getCategory(request, cat):
    products = Product.objects.filter(category=cat)
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def register(request):
    data = request.data
    hashed_password = make_password(data['password'])
    user = User.objects.create(
       username = data['username'],
       password = hashed_password
    )
    serializer = UserSerializer(user, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def login(request):
    data = request.data
    user = Product.objects.get(username=data['username'])
    check = check_password(data['password'], user['password'])
    if(check):
        serializer = UserSerializer(user, many=False)
        return Response(serializer.data)
    else:
        return Response('Incorrect password')