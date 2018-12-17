from django.urls import path
from . import views

urlpatterns=[
    path('', views.main_f, name='main_f'),
]
