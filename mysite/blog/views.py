from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Comment
from django.views.generic import View
from .forms import PostForm, CommentForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator


# def blog(request):
#     posts = Post.objects.all()
#     return render(request, 'blog/blog.html', context = {'posts': posts})

class Blog(View):
    def get(self, request):
        posts = Post.objects.all()
        return render(request, 'blog/blog.html', context = {'posts': posts})

class BlogDetails(View):
    def get(self, request, pk):
        details = Post.objects.get(pk=pk)
        comments = details.comments.filter(active = True)
        pagi = Paginator(comments, 2)
        page_number = request.GET.get('page', 1)
        page = pagi.get_page(page_number)
        is_paginated = page.has_other_pages()

        if page.has_previous():
            prev_url = '?page={}'.format(page.previous_page_number())
        else:
            prev_url = ''

        if page.has_next():
            next_url = '?page={}'.format(page.next_page_number())
        else:
            next_url = ''

        context = {'comments': page, 'details': details, 'prev_url': prev_url, 'next_url': next_url}

        if request.POST:
            return context
        else:
            return render(request, 'blog/blog_details.html', context = context)

    def post(self, request, pk):
        context = self.get(request, pk)
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
