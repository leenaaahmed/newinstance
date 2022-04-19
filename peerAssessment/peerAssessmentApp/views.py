from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from .forms import SignUpForm, CourseForm, RegistryForm, TeamForm, ContactForm
from .models import SiteUsers, Registry, Course, Team, Question, Answer, Submission, Choice, Assessment
from django.contrib import messages
from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.conf import settings
from django.core.mail import send_mail
from django.core import mail
from django.template import loader
from django.utils.html import strip_tags
from django.forms.formsets import formset_factory
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
import random
# Create your views here.

def home_view(request):
    return render(request,'home.html')

@csrf_protect
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            access_code=form.cleaned_data.get('access_code')
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password1')
            email = form.cleaned_data.get('email')
            user=authenticate(username=username, password=password)
            date_of_birth=form.cleaned_data.get('date_of_birth')
            student = SiteUsers.objects.create(user=user, date_of_birth=date_of_birth, email = email)

            course = Course.objects.get(access_code=access_code)
            if (course):
                course.students.add(student)
            messages.success(request, 'Account Created')
        else:
            messages.error(request, "Unsuccessful registration. Invalid information.")
    form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

@login_required
def my_redirect(request):
    if request.user.siteusers.types == "pro":
        return redirect('/Dashboards/prodashboard')
    else:
         return redirect('/Dashboards/studashboard')


def prodashboard(request):
    return render(request, 'Dashboards/prodashboard.html')

def studashboard(request):
    courses = Course.objects.all()
    team = Team.objects.all()
    person = request.user
    users = SiteUsers.objects.get(user=person)
    cassess = Cassess.objects.all()
    return render(request, 'Dashboards/studashboard.html', {'team': team, 'cassess': cassess, 'courses:':courses, 'users': users})

def student_or_professor(request):
    return render(request, 'student_or_professor.html')

def about(request):
    return render(request, 'about.html')

def add_course(request):
    submitted = False
    if request.method == "POST":
        form = CourseForm(request.POST)
        if form.is_valid():
            course = form.save()
            course.admins.add(request.user)
            course.access_code = random.randint(10000,99999)
            course.save()
            return HttpResponseRedirect('/add_course?submitted=True')
    else:
        form = CourseForm
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'add_course.html', {'form':form, 'submitted':submitted})

def add_admin(request):
    submitted = False
    if request.method == "POST":
        form = RegistryForm(request.POST)
        if form.is_valid():
            admin = form.cleaned_data.get('admin')
            course_id = form.cleaned_data.get('course_id')
            current_course = Course.objects.get(course_id=course_id)
            current_course.admins.add(admin)
            return HttpResponseRedirect('/add_admin?submitted=True')
    else:
        form = RegistryForm
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'add_admin.html', {'form':form, 'submitted':submitted})

def view_courses(request):
    course_list = Course.objects.all()

    return render(request,'view_courses.html', {'course_list': course_list})

def create_assessment(request):
    submitted = False
    if request.method == "POST":
        form = CassessForm(request.POST)
        print('form: ', form)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add_questions')
    else:
        form = CassessForm
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'create_assessment.html', {'form':form, 'submitted':submitted})
# add students and teams to a course
def add_teams(request):
    submitted = False
    if request.method == "POST":
        user = request.POST["memebers"]
        form = TeamForm(request.POST)
        if form.is_valid():
            form.save()
        students = SiteUsers.objects.all()
        for user in students:

            subject = "You have been Registered to a Team and Course"
            message = ''
            email_from = settings.EMAIL_HOST_USER
            recipient_list = {user.email,}
            html_message = loader.render_to_string(
                        'email.html',
                        {
                        'context':'values',
                        'user_name': user.user
                        }
                    )

            send_mail(subject, message, email_from, recipient_list, html_message = html_message)
        return HttpResponseRedirect('/add_teams?submitted=True')

    else:
        form = TeamForm
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'add_teams.html', {'form':form, 'submitted':submitted})


def add_questions(request):
    submitted = False
    if request.method == "POST":
        form = QuestionForm(request.POST)
        print('form: ', form)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/choose_response')
    else:
        form = QuestionForm
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'add_questions.html', {'form':form, 'submitted':submitted})

def choose_response(request):
    return render(request,'choose_response.html')


def oe_response(request):
    submitted = False
    if request.method == "POST":
        form = ResponseForm(request.POST)
        print('form: ', form)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add_questions')
    else:
        form = ResponseForm
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'oe_response.html', {'form':form, 'submitted':submitted})

def mc_response(request):
    submitted = False
    if request.method == "POST":
        form = MCResponseForm(request.POST)
        print('form: ', form)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add_questions')
    else:
        form = MCResponseForm
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'mc_response.html', {'form':form, 'submitted':submitted})

def view_assessment(request, ):
    '''Grab all assessments, questions, resposnes'''
    person = request.user
    user = SiteUsers.objects.get(user =person)
    team = Team.objects.all()
    assess = Cassess.objects.all()
    reg = Registry.objects.all()
    question = Question.objects.all()
    mc = MCResponse.objects.all()
    oe = Response.objects.all()
    submitted = False
    if request.method == "POST":
        for a in assess:
            for q in question:
                if q.assessment == a:
                    for b in mc:
                        if b.question == q and b.mc == '':
                            instance = MCResponse(question = q, mc = request.POST['mc'], responder = user)
                            instance.save()
                    for c in oe:
                        if c.question == q and c.response == '':
                            inst=Response(question = q, response = request.POST['response'], responder = user)
                            inst.save()
        return HttpResponseRedirect('/view_assessment?submitted=True')

    else:
        forma = MCResponseForm
        formb = ResponseForm
        if 'submitted' in request.GET:
            submitted = True


    return render(request, 'view_assessment.html', {'assess': assess, 'question':question, 'team': team, 'mc': mc, 'oe': oe, 'forma':forma, 'formb':formb, 'submitted':submitted})

def contact(request):
	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			subject = "Website Inquiry"
			body = {
			'first_name': form.cleaned_data['first_name'],
			'last_name': form.cleaned_data['last_name'],
			'email': form.cleaned_data['email_address'],
			'message':form.cleaned_data['message'],
			}
			message = "\n".join(body.values())

			try:
				send_mail(subject, message, 'newinstanceco@gmail.com', ['newinstanceco@gmail.com'])
			except BadHeaderError:
				return HttpResponse('Invalid header found.')


	form = ContactForm()
	return render(request, "contact.html", {'form':form})

# def view_course_detail(request, course_id):
    # path = request.path
    # course_id = path.split('/')[3]
    # course = Course.objects.get(course_id=course_id)
    #course_id = course_id

    # teams = Team.objects.filter(course=course)
    # return render(request, 'view_course_detail.html', {'course':course, 'teams': teams})
