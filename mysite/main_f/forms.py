from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError



class PassForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']


    def __init__(self, *args, **kwargs):
        super(PassForm, self).__init__(*args, **kwargs)
            
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'


        # widgets = {
        #     'username': forms.TextInput(attrs={'class': 'userinp', 'placeholder': 'Имя пользователя'}),
        #     'email': forms.EmailInput(attrs={'class': 'userinp', 'placeholder': 'Электронная почта'}),
        #     'password1': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'пароль'}),
        #     'password2': forms.PasswordInput(attrs={'class': 'form-control'})
        # }
