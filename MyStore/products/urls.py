from django import urls
from . import views
from django.urls import path , include

app_name="products"
urlpatterns = [
    path('' , views.products , name="products"),
    path('<slug>' , views.product_detail , name="product-detail")
]
