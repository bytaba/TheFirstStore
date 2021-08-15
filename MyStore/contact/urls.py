from django import urls
from . import views
from django.urls import path , include

app_name = "contact"
urlpatterns = [
    path('' , views.contact , name="contact")
]
