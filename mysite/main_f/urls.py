from django.urls import path
from . import views

# urlpatterns=[
#     path('', views.PassCreate.as_view(), name='pass_create'),
# ]

urlpatterns = [
    path('pass_create/', views.PassCreate.as_view(), name='pass_create'),
    path('', views.main_f, name='main_f'),
    path('pass_enter/', views.PassEnter.as_view(), name='pass_enter'),
    path('pass_logout/', views.passlogout, name='pass_logout'),
]
