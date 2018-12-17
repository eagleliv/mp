from django.urls import path
from . import views

urlpatterns=[
    path('', views.m_scr, name='m_scr'),
]
