#
# class PassCreate(FormView):
#     form_class = UserCreationForm
#     success_url ='/'
#     template_name = 'main_f/register.html'
#     def form_valid (self, form):
#         form.save()
#         return super(PassCreate, self).form_valid(form)
#
# class PassEnter(FormView):
#     form_class = AuthenticationForm
#     success_url = '/'
#     template_name = 'main_f/login.html'
#     def form_valid(self, form):
#         self.user = form.get_user()
#         login(self.request, self.user)
#         return super(PassEnter, self).form_valid(form)

from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, get_user, logout
from django.views.generic.edit import FormView
from .forms import PassForm
from django.core.exceptions import ValidationError
from django.contrib.auth import authenticate


def main_f(request):
    return render (request, 'main_f/main_f.html')


class PassCreate(FormView):
    def get(self, request):
        form = PassForm() #UserCreationForm()
        return render(request, 'main_f/register.html', context={'form': form})
    def post(self, request):
        form = PassForm(request.POST) #UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            user_n = form.cleaned_data.get('username')
            user_p = form.cleaned_data.get('password1')
            user = authenticate(username = user_n, password = user_p)
            login(request, user)
            return redirect('/')
        return render(request, 'main_f/register.html', context={'form': form})



class PassEnter(FormView):
    def get(self, request):
        if get_user(request).is_authenticated:
            return redirect('/')
        else:
            form = AuthenticationForm()
            return render(request, 'main_f/login.html', context={'form': form})
    def post(self, request):
        form = AuthenticationForm(None, request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('/')
        return render(request, 'main_f/login.html', context={'form': form})

def passlogout(request):
    logout(request)
    return redirect('/')
