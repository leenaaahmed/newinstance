from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
import datetime

class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length = 40, help_text = 'Required')
    date_of_birth = forms.DateField(initial = datetime.date.today,help_text = 'Required')

    class Meta:
        model = User
        fields = ('username','email', 'date_of_birth', 'password',  'password')
        