from django.shortcuts import render, redirect
from .forms import SignUpForm

from .models import SiteUsers
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import HttpResponse

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
            login(request, user)
            messages.success(request, 'Account Created')
        else:
            messages.error(request, "Unsuccessful registration. Invalid information.")
    form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(usernname=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                # return render(request, 'home.html')
            else:
                messages.error(request, 'Invalid username or password')
        else:
            messages.error(request, 'Invalid username or password')
            form = AuthenticationForm()
    form = AuthenticationForm()
    return render(request=request, template_name="registration/login.html", context={"login_form":form})
    # return render(request, 'signup.html', {'form': form})
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
    return HttpResponse('<h1> Home Page Test</h1>')