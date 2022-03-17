from django.shortcuts import render
from .forms import SignUpForm
from django.contrib import messages
from django.views.decorators.csrf import csrf_protect

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

