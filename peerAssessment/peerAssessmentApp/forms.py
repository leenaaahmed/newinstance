from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
import datetime
from django.forms import ModelForm
from .models import Course, Registry, Cassess, Team, SiteUsers,Question,Response, MCResponse


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
            'User': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Professor Name'} ),
            'course': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Course Name'} ),
        }

class CassessForm(ModelForm):
    class Meta:
        model = Cassess
        fields = ('assess_number', 'due_date', 'publish_date', 'course')
        labels = {
            'assess_number': '',
            'due_date': '',
            'publish_date': '',
            'course': '',
        }
        widgets = {
            'assess_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Assessment Number'}),
            'due_date': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Due Date'}),
            'publish_date': forms.TextInput(attrs={'class': 'forms-control','placeholder': 'Publish Date'}),
            'course': forms.Select(attrs={'class': 'forms-control','placeholder': 'Course'}),
        }

class TeamForm(ModelForm):
    class Meta:
        model = Team
        fields = ('team_name', 'course', 'memebers')
        labels = {

            'team_name': '', 
            'course': '', 
            'memebers': '',
        }
        widgets = {
            'Team Name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Team Name'} ),
            'course': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Course'} ),
            'memebers': forms.SelectMultiple(attrs={'class': 'form-control', 'placeholder': 'Members'} ),

        }

class QuestionForm(ModelForm):
    class Meta:
        model = Question
        fields = ('assessment', 'question')
        labels = {

            'assessment': '', 
            'question': '', 
            
        }
        widgets = {
            'assessment': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Assessment'} ),
            'question': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Question'} ),
        }

class ResponseForm(ModelForm):
    class Meta:
        model = Response
        fields = ('assessment', 'response', 'question')
        labels = {

            'assessment': '', 
            'response': '', 
            'question': '',
            
            
        }
        widgets = {
            'assessment': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Assessment'} ),
            'response': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Response'} ),
            'question': forms.Select(attrs={'class': 'form-control', 'placeholder': 'question'} ),
            
         } 

class MCResponseForm(ModelForm):
    class Meta:
        model = MCResponse

        fields = ('assessment', 'mc', 'question')
        labels = {

            'assessment': '', 
            'mc': '', 
            'question': '',
            
        }
        widgets = {
            'assessment': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Assessment'} ),
            'mc': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Assessment'} ),
            'question': forms.Select(attrs={'class': 'form-control', 'placeholder': 'question'} ),

         } 



