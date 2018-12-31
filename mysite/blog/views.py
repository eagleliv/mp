from django.shortcuts import render, get_object_or_404
from .models import Post
#from django.http import HttpResponse


def blog(request):
    posts = Post.objects.all()
    return render(request, 'blog/blog.html', context = {'posts': posts})

def blog_details(request, pk):
        details = get_object_or_404(Post, pk=pk)
        return render(request, 'blog/blog_details.html', context = {'details': details})
