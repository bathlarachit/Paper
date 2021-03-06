from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms
from eapp import models
#########
class UserCreateForm(UserCreationForm):
    class Meta:
        fields =('first_name','last_name','username','email','password1','password2')
        model = get_user_model()
