from django import forms
from django.contrib.auth.models import User


class UserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password')
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder':"votre prenom"}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder':"votre nom "}),
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder':"votre nom d'utilisateur"}),
            'email': forms.TextInput(attrs={'class': 'form-control', 'placeholder':"votre Email"}),
            'password': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder':"votre mot de pass"}),
        }


class UserLoginForm(forms.Form):
    username = forms.CharField(required=True, max_length=50, min_length=3 ,  widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':"votre nom d'utilisateur"}))
    password = forms.CharField(required=True, max_length=50, min_length=3 , widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder':'votre mot de pass'}))

   

   
