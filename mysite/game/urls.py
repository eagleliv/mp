from . import views
from django.urls import path

urlpatterns = [
    path('', views.Game.as_view(), name='game'),
]
