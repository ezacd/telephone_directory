from django import forms
from .models import User
from allauth.account.forms import LoginForm


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'post', 'address', 'communications', 'organization', 'password']
