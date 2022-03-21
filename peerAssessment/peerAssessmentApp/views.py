from django.shortcuts import render
from .forms import SignUpForm
from django.contrib import messages
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import HttpResponse

# Create your views here.

@csrf_protect
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account Created')
            return render(request, 'signup.html')

    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})
#not working currently


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