from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
import datetime
from django.forms import ModelForm
from .models import Course, Registry


class SignUpForm(UserCreationForm):
    username = forms.CharField(help_text='Required')
    email = forms.EmailField(max_length = 40, help_text = 'Required')
    date_of_birth = forms.DateField(initial = datetime.date.today,help_text = 'Required')
    access_code = forms.CharField(max_length = 5, help_text='Required')

    class Meta:
        model = User
        fields = ('username','email', 'date_of_birth', 'password1', 'password2')


class CourseCreation(forms.Form):
    course = forms.CharField(max_length = 40, help_text = 'Description')
    course_id = forms.CharField(max_length = 10, help_text = 'Required')
    year = forms.CharField(max_length = 4, help_text = 'Required')
    semester = forms.CharField(max_length = 1, help_text = 'S or F')
    class Meta:
        ##model = Course
        fields = ('course', 'course_id', 'year', 'semester')

#class GroupCreation(forms.Form):
 #   course = forms.CharField(max_length = 40, help_text = 'Required')
  #  group_name = forms.CharField(max_length = 20, help_text = 'Required')
   # class Meta:
    #    fields = ('course', 'group_name')

class CourseForm(ModelForm):
    class Meta:
        model = Course
        fields = ('course', 'course_id', 'year', 'semester')
        labels = {

            'course': '',
            'course_id':'',
            'year': '',
            'semester': '',

        }
        widgets = {
            'course': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Course Name'} ),
            'course_id': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Course ID'} ),
            'year': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Year'} ),
            'semester': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Semester'} ),
        }

class RegistryForm(ModelForm):
    class Meta:
        model = Registry
        fields = ('User','course')
        labels = {

            'User': '',
            'course': '',
        }
        widgets = {
            'User': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Course Name'} ),
            'course': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Professor Name'} ),
        }