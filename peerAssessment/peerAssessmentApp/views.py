from django.shortcuts import render, HttpResponse, redirect
from .forms import SignUpForm, CourseForm, RegistryForm
from .models import SiteUsers, Enrollment, Registry
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect

# Create your views here.

@csrf_protect
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password1')
            user=authenticate(username=username, password=password)
            date_of_birth=form.cleaned_data.get('date_of_birth')
            SiteUsers.objects.create(user=user, date_of_birth=date_of_birth)
            messages.success(request, 'Account Created')
        else:
            messages.error(request, "Unsuccessful registration. Invalid information.")
    form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def createUser(request):
    if request.method=='POST':
        form = UserCreationForm()
        if form.is_valid():
            form.save()
            return render(request, 'signup.html')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})


def courseCreation(request):
    if request.method == 'POST':
        form = CourseCreation(request.POST)
        if form.is_valid():
            form.save()
            message.success(request, 'Course Created')
            return render(request, 'course.html')
    else:
        form = CourseCreation()
    return render(request, 'course.html', {'form': form})




def home_view(request):
    return render(request,'home.html')

@login_required
def my_redirect(request):
    if request.user.siteusers.type =="stu":
        return redirect('/Dashboards/studashboard')
    if request.user.siteusers.type == "pro":
        return redirect('/Dashboards/prodashboard')


def prodashboard(request):
    course_list = Registry.objects.all()
    return render(request, 'Dashboards/prodashboard.html', {'course_list':course_list})

def studashboard(request):
    course_list = Registry.objects.all()
    return render(request, 'Dashboards/studashboard.html', {'course_list':course_list})

def student_or_professor(request):
    return render(request, 'student_or_professor.html')
def about(request):
    return render(request, 'about.html')
def contact(request):
    return render(request, 'contact.html')

def add_course(request):
    submitted = False
    if request.method == "POST":
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add_course?submitted=True')
    else:
        form = CourseForm
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'add_course.html', {'form':form, 'submitted':submitted})

def add_professor(request):
    submitted = False
    if request.method == "POST":
        form = RegistryForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add_professor?submitted=True')
    else:
        form = RegistryForm
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'add_professor.html', {'form':form, 'submitted':submitted})