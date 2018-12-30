from django.urls import path
from . import views


urlpatterns=[
    path('', views.blog, name='blog'),
    path('post/<pk>/', views.blog_details, name='blog_details'),
]
