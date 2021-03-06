from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Comment
from django.views.generic import View
from .forms import PostForm, CommentForm
from django.contrib.auth.mixins import LoginRequiredMixin
from .utils import *



# def blog(request):
#     posts = Post.objects.all()
#     return render(request, 'blog/blog.html', context = {'posts': posts})

class Blog(View):
    def get(self, request):
        posts = Post.objects.all()
        return pagi_nator(request, 6, posts)


class BlogDetails(View):
    def get(self, request, pk):
        details = Post.objects.get(pk=pk)
        comments = details.comments.filter(active = True)
        return pagi_nator(request, 2, comments, details)

    def post(self, request, pk):
        context = self.get(request, pk)
        details = context['details']
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit = False)
            new_comment.post = details
            new_comment.name = request.user.username
            new_comment.save()
            return redirect('blog_details', pk=pk)
        context['comment_form'] = comment_form
        return render(request, 'blog/blog_details.html', context = context)


class PostCreate(LoginRequiredMixin, View):
    raise_exception = True
    def get(self, request):
        form = PostForm()
        return render(request, 'blog/post_create.html', context={'form': form})
    def post(self, request):
        bound_form = PostForm(request.POST)
        if bound_form.is_valid():
            new_post = bound_form.save(commit = False)
            new_post.author = request.user.username
            new_post = bound_form.save()
            return redirect('blog_details', pk=new_post.id)
        return render(request, 'blog/post_create.html', context={'form': bound_form})

class PostUpdate(LoginRequiredMixin, View):
    raise_exception = True
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

class PostDelete(LoginRequiredMixin, View):
    raise_exception = True
    def get(self, request, pk):
        post = Post.objects.get(pk=pk)
        return render(request, 'blog/post_delete.html', context={'post': post})
    def post(self, request, pk):
        post = Post.objects.get(pk=pk)
        post.delete()
        return redirect ('blog')

def my_posts(request):
    posts = Post.objects.filter(author = request.user.username)
    return render(request, 'blog/blog.html', context = {'posts': posts})
