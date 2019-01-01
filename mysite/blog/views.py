from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from django.views.generic import View
from .forms import PostForm
#from django.http import HttpResponse


def blog(request):
    posts = Post.objects.all()
    return render(request, 'blog/blog.html', context = {'posts': posts})

def blog_details(request, pk):
        details = get_object_or_404(Post, pk=pk)
        return render(request, 'blog/blog_details.html', context = {'details': details})

class PostCreate(View):
    def get(self, request):
        form = PostForm()
        return render(request, 'blog/post_create.html', context={'form': form})
    def post(self, request):
        bound_form = PostForm(request.POST)
        if bound_form.is_valid():
            new_post = bound_form.save()
            return redirect('blog_details', pk=new_post.id)
        return render(request, 'blog/post_create.html', context={'form': bound_form})

class PostUpdate(View):
    def get(self, request, pk):
        post = Post.objects.get(pk = pk)
        bound_form = PostForm(instance=post)
        return render(request, 'blog/post_update.html', context = {'form': bound_form, 'post': post})
    def post(self, request, pk):
        post = Post.objects.get(pk = pk)
        bound_form = PostForm(request.POST, instance=post)
        if bound_form.is_valid():
            new_post = bound_form.save()
            return redirect('blog_details', pk=new_post.id)
        return render(request, 'blog/post_update.html', context={'form': bound_form, 'post': post})

class PostDelete(View):
    def get(self, request, pk):
        post = Post.objects.get(pk=pk)
        return render(request, 'blog/post_delete.html', context={'post': post})
    def post(self, request, pk):
        post = Post.objects.get(pk=pk)
        post.delete()
        return redirect ('blog')
