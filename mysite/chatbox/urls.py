from django.urls import path
from . import views

urlpatterns = [
    path('', views.chatdetails, name='chat_form'),
    path('<room_name>/', views.room, name='room'),
]
