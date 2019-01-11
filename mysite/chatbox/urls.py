from django.urls import path
from . import views

urlpatterns = [
    path('', views.ChatDetails.as_view(), name='chat_form'),
]
