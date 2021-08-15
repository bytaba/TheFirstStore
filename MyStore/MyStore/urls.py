#from MyStore.TheFirstStore.MyStore.about.views import about
from django import urls
from django.contrib import admin
from django.urls import path , include
from . import views

app_name = "main"
urlpatterns = [
    path('admin/', admin.site.urls),
    path(''                 , views.index              , name="main"    ),
    path('about-us/'        , include('about.urls')    , name="about"    ),
    path('contact-us/'      , include('contact.urls')  , name="contact"  ),
    path('products/'        , include('products.urls') , name="products" ),
    path('accounts/'        , include('accounts.urls') , name="accounts" )
]
