from pyexpat import model
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import User


class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "password1", "password2")
