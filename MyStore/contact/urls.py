from django import urls
from . import views
from django.urls import path , include


urlpatterns = [
    path('' , views.contact)
]
