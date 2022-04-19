from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
import datetime
from django.forms import ModelForm
from .models import Course, Registry, Team, SiteUsers,Question, Answer, Assessment, Choice, Submission


class SignUpForm(UserCreationForm):
    username = forms.CharField(help_text='Required')
    email = forms.EmailField(max_length = 40, help_text = 'Required')
    date_of_birth = forms.DateField(initial = datetime.date.today,help_text = 'Required')
    access_code = forms.CharField(max_length = 5, help_text='Required')
    class Meta:
        model = User
        fields = ('username','email', 'date_of_birth', 'password1', 'password2', 'access_code')
class CourseForm(ModelForm):
    class Meta:
        model = Course
        fields = ('course_name', 'course_id', 'year', 'semester')
        labels = {

            'course_name': '',
            'course_id':'',
            'year': '',
            'semester': '',

        }

        YEAR_CHOICES = {
            ("2021", "2021"),
            ("2022", "2022"),
            ("2023", "2023"),
            ("2024", "2024"),
        }
        SEMESTER_CHOICES = {
            ("Fall", "FALL"),
            ("Spring", "SPRING"),
        }
        widgets = {
            'course_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Course Name'} ),
            'course_id': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Course ID'} ),
            'year': forms.Select(choices=YEAR_CHOICES, attrs={'class': 'form-control', 'placeholder': 'Year'} ),
            'semester': forms.Select(choices=SEMESTER_CHOICES, attrs={'class': 'form-control', 'placeholder': 'Semester'}),
        }

class RegistryForm(ModelForm):
    class Meta:
        model = Registry
        fields = ('course_id','admin')
        labels = {
            'course_id': '',
            'admin': '',
        }
        widgets = {
            'course_id': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Course Name', 'help_text': 'Course ID'} ),
            #'admin': forms.SelectMultiple(attrs={'class': 'form-control', 'required': 'true', 'help_text': 'Admin'} ),
            'admin': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Select Admin'} ),
        }

# class CassessForm(ModelForm):
#     class Meta:
#         model = Cassess
#         fields = ('assess_number', 'due_date', 'publish_date', 'course')
#         labels = {
#             'assess_number': '',
#             'due_date': '',
#             'publish_date': '',
#             'course': '',
#         }
#         widgets = {
#             'assess_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Assessment Number'}),
#             'due_date': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Due Date'}),
#             'publish_date': forms.TextInput(attrs={'class': 'forms-control','placeholder': 'Publish Date'}),
#             'course': forms.Select(attrs={'class': 'forms-control','placeholder': 'Course'}),
#         }

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

# class QuestionForm(ModelForm):
#     class Meta:
#         model = Question
#         fields = ('assessment', 'question')
#         labels = {

#             'assessment': '',
#             'question': '',

#         }
#         widgets = {
#             'assessment': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Assessment'} ),
#             'question': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Question'} ),
#         }

# class ResponseForm(ModelForm):
#     class Meta:
#         model = Response
#         fields = ('response', 'question')
#         labels = {

#             'response': '',
#             'question': '',


#         }
#         widgets = {
#             'response': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Response'} ),
#             'question': forms.Select(attrs={'class': 'form-control', 'placeholder': 'question'} ),

#          }

# class MCResponseForm(ModelForm):
#     class Meta:
#         model = MCResponse

#         fields = ('mc', 'question')
#         labels = {

#             'mc': '',
#             'question': '',

#         }
#         widgets = {
#             'mc': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Multiple Choice Response'} ),
#             'question': forms.Select(attrs={'class': 'form-control', 'placeholder': 'question'} ),

#          }

class ContactForm(forms.Form):
	first_name = forms.CharField(max_length = 50)
	last_name = forms.CharField(max_length = 50)
	email_address = forms.EmailField(max_length = 150)
	message = forms.CharField(widget = forms.Textarea, max_length = 2000)
