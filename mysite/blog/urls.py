from django.urls import path
from . import views
from .models import Post


urlpatterns=[
    path('', views.blog, name='blog'),
    path('<post_id>', views.blog_details, name='blog_details'),
]
