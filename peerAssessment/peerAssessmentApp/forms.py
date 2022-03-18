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
        

class CourseCreation(forms.Form):
    course = forms.CharField(max_length = 40, help_text = 'Description')
    course_id = forms.CharField(max_length = 10, help_text = 'Required')
    year = forms.CharField(max_length = 4, help_text = 'Required')
    semester = forms.CharField(max_length = 1, help_text = 'S or F')

    class Meta:
        ##model = Course
        fields = ('course', 'course_id', 'year', 'semester')