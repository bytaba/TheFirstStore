from django import urls
from django.urls import path 
from . import views


app_name = "blog"
urlpatterns = [
    path( ''        , views.posts        , name="posts"         ),
    path( '<slug>'  , views.post_detail  , name="post-detail"   )
]