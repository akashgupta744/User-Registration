from django import forms
from .models import *


class UserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','email','password']
        widgets={'password':forms.PasswordInput}
        help_texts = {'username':''}

class ProfileForm(forms.ModelForm):
    class Meta:
        model=Profile
        fields=['add','pic']

