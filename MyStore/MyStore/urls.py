#from MyStore.TheFirstStore.MyStore.about.views import about
from django.contrib import admin
from django.urls import path , include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('about-us/' , include('about.urls') )
]
