from django.urls import path
from . import consumers


websocket_urlpatterns = [
    path('ws/chatbox/<room_name>/', consumers.ChatConsumer),
]
