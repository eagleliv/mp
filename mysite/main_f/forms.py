from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



# class PassForm(UserCreationForm):
#     email = forms.EmailField(max_length = 254)
#     class Meta:
#         model = User
#         fields = ['username', 'email', 'password1', 'password2']
#
#         widgets = {
#             'username': forms.TextInput(attrs={'class': 'userinp', 'placeholder': 'Имя пользователя'}),
#             'email': forms.EmailInput(attrs={'class': 'userinp', 'placeholder': 'Электронная почта'}),
#             'password1': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'пароль'}),
#             'password2': forms.PasswordInput(attrs={'class': 'form-control'})
#         }


class PassForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'userinp', 'placeholder': 'username'}),
            'password1': forms.PasswordInput(attrs={'class': 'userinp'}),
        }
