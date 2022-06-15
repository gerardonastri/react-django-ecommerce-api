from django.urls import path
from . import views

urlpatterns = [
    path('', view=views.getRoutes, name="routes"),
    path('products/',  views.getProducts, name="products"),
    path('products/create/', views.createProduct, name="create-product"),
   # path('products/<str:pk>/update/', views.updateproduct, name="update-product"),
    #path('products/<str:pk>/delete/', views.deleteproduct, name="delete-product"),
    path('products/<str:pk>',  views.getProduct, name="product"),
    path('products/category/<str:cat>',  views.getCategory, name="product"),
    path('auth/register/',  views.register, name="register"),
    path('auth/login/',  views.login, name="login")
]