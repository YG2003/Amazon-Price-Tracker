from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)
    
    username = forms.CharField(widget=forms.TextInput(attrs={
        "class":"input",
        "type":"text",
        "placeholder":"Enter Username"
    }))

    password = forms.CharField(widget=forms.TextInput(attrs={
        "class":"input",
        "type":"password",
        "placeholder":"Enter Password"
    }))


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    username = forms.CharField(widget=forms.TextInput(attrs={
        "class":"input",
        "type":"text",
        "placeholder":"Enter Username"
    }))

    email = forms.CharField(widget=forms.TextInput(attrs={
        "class":"input",
        "type":"email",
        "placeholder":"Enter E-mail Id"
    }))

    password1 = forms.CharField(widget=forms.TextInput(attrs={
        "class":"input",
        "type":"password",
        "placeholder":"Enter Password"
    }))

    password2 = forms.CharField(widget=forms.TextInput(attrs={
        "class":"input",
        "type":"password",
        "placeholder":"Re-Enter Password"
    }))

    class Meta:
        model = User
        fields = ['username', 'email','password1', 'password2']
        