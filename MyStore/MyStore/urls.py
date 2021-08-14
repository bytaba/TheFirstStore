#from MyStore.TheFirstStore.MyStore.about.views import about
from django import urls
from django.contrib import admin
from django.urls import path , include
from . import views

app_name = "index"
urlpatterns = [
    path('admin/', admin.site.urls),
    path('' , views.index  , name="index"),
    path('about-us/' , include('about.urls') ),
    path('contact-us/' , include('contact.urls')),
    path('products/'   , include('products.urls')),
    path('accounts/' , include('accounts.urls'))
]
