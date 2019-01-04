# from django.shortcuts import render
# from .models import PassBase
# from django.views.generic import View
# from .forms import PassForm
#
#
# class PassCreate(View):
#     def get(self, request):
#         pass_data = PassForm()
#         return render(request, 'main_f/main_f.html', context = {'pass_data': pass_data})
#     def post(self, request):
#         bound_form = PassForm(request.POST)
#         if bound_form.is_valid():
#             if name_u in PassBase.objects.all():
#                 return render(request, 'main_f/main_f.html', context = {'name': name_u})

from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from django.views.generic.edit import FormView
from .forms import PassForm
from django.core.exceptions import ValidationError

def main_f(request):
    return render (request, 'main_f/main_f.html')


class PassCreate(FormView):
    form_class = PassForm
    success_url ='/'
    template_name = 'main_f/register.html'
    def form_valid (self, form):
        form.save()
        return super(PassCreate, self).form_valid(form)

class PassEnter(FormView):
    form_class = AuthenticationForm
    success_url = '/'
    template_name = 'main_f/login.html'
    def form_valid(self, form):
        self.user = form.get_user()
        login(self.request, self.user)
        return super(PassEnter, self).form_valid(form)

# class PassCreate(FormView):
#     def get(self, request):
#         form = PassForm()
#         return render(request, 'main_f/register.html', context={'form': form})
#     def post(self, request):
#         form = PassForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('/')
#         else:
#             form = PassForm()
#         return render(request, 'main_f/register.html', context={'form': form})
#
# class PassEnter(FormView):
#     def get(self, request):
#         form = AuthenticationForm()
#         return render(request, 'main_f/login.html', context={'form': form})
#     def post(self, request):
#         form = AuthenticationForm(request.POST)
#         if form.is_valid():
#             user = form.get_user(request)
#             login(request, user)
#             return redirect('/')
#         else:
#             form = AuthenticationForm()
#             print(form.cleaned_data())
#         return render(request, 'main_f/login.html', context={'form': form})
