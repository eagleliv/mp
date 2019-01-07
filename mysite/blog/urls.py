from django.urls import path
from . import views


urlpatterns=[
    path('', views.blog, name='blog'),
    path('create/', views.PostCreate.as_view(), name='post_create'),
    path('post/<pk>/update/', views.PostUpdate.as_view(), name='post_update'),
    path('post/<pk>/delete/', views.PostDelete.as_view(), name='post_delete'),
    path('post/<pk>/', views.blog_details, name='blog_details'),
    path('my_posts/', views.my_posts, name='my_posts'),
]
