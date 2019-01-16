from django.urls import path
from . import views


urlpatterns=[
    path('', views.Blog.as_view(), name='blog'),
    path('create/', views.PostCreate.as_view(), name='post_create'),
    path('post/<pk>/update/', views.PostUpdate.as_view(), name='post_update'),
    path('post/<pk>/delete/', views.PostDelete.as_view(), name='post_delete'),
    path('post/<pk>/', views.BlogDetails.as_view(), name='blog_details'),
    path('my_posts/', views.my_posts, name='my_posts'),
]
