from django import urls
from . import views
from django.urls import path , include

app_name="products"
urlpatterns = [
    path('' , views.products , name="products")
]
