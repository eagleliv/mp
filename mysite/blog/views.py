from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Comment
from django.views.generic import View
from .forms import PostForm, CommentForm
#from django.http import HttpResponse


def blog(request):
    posts = Post.objects.all()
    return render(request, 'blog/blog.html', context = {'posts': posts})

# def blog_details(request, pk):
#         details = get_object_or_404(Post, pk=pk)
#         comments = details.comments.filter(active = True)
#
#         if request.method == 'POST':
#             comment_form = CommentForm(request.POST)
#             if comment_form.is_valid():
#                 new_comment = comment_form.save(commit = False)
#                 new_comment.post = details
#                 new_comment.save()
#         else:
#             comment_form = CommentForm()
#
#         return render(request, 'blog/blog_details.html', context = {'details': details, 'comments': comments, 'comment_form': comment_form})

class BlogDetails(View):
    def get(self, request, pk):
        details = Post.objects.get(pk=pk)
        comments = details.comments.filter(active = True)
        return render(request, 'blog/blog_details.html', context = {'comments': comments, 'details': details})
    def post(self, request, pk):
        comment_form = CommentForm(request.POST)
        details = Post.objects.get(pk=pk)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit = False)
            new_comment.post = details
            new_comment.name = request.user.username
            new_comment.save()
            return redirect('blog_details', pk=pk)
        return render(request, 'blog/blog_details.html', context = {'comment_form': comment_form})


class PostCreate(View):
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

def my_posts(request):
    posts = Post.objects.filter(author = request.user.username)
    return render(request, 'blog/blog.html', context = {'posts': posts})
