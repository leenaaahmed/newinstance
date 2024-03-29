from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from .forms import SignUpForm, CourseForm, RegistryForm, CassessForm, TeamForm, QuestionForm, ResponseForm, MCResponseForm, ContactForm,SubmissionForm, EnrollForm
from .models import SiteUsers, Registry, Course, Cassess, Team, Question, Response, MCResponse, Submission
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm
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
from datetime import datetime, timedelta
# Create your views here.

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
            student = SiteUsers.objects.create(user=user, date_of_birth=date_of_birth, email=email)
            course = Course.objects.get(access_code=access_code)
            if (course):
                course.students.add(student)
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
    if request.user.siteusers.types == "pro":
        return redirect('/Dashboards/prodashboard')
    else:
         return redirect('/Dashboards/studashboard')


def prodashboard(request):
    course_list = Registry.objects.all()
    return render(request, 'Dashboards/prodashboard.html', {'course_list':course_list})

def studashboard(request):
    courses = Course.objects.all()
    team = Team.objects.all()
    person = request.user
    users = SiteUsers.objects.get(user=person)
    cassess = Cassess.objects.all()
    x = datetime.now().date()
    i = []
    for c in cassess:
        for t in team:
            if t.course == c.course:
                for user in t.memebers.all():
                    if users == user:
                        assess = c
                        if assess.due_date < datetime.now().date():
                            i.append(assess.assess_number)

    return render(request, 'Dashboards/studashboard.html', {'team': team, 'cassess': cassess, 'courses:':courses, 'users': users, 'i': i, 'x':x})

def student_or_professor(request):
    return render(request, 'student_or_professor.html')
def about(request):
    return render(request, 'about.html')
def reviews(request):
    return render(request, 'reviews.html')
def contact(request):
    return render(request, 'contact.html')
def stu_view_team(request):
    return render(request, 'stu_view_team.html')

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

def add_professor(request):
    submitted = False
    if request.method == "POST":
        form = RegistryForm(request.POST)
        if form.is_valid():
            admin = form.cleaned_data.get('admin')
            course = form.cleaned_data.get('course')
            current_course = Course.objects.get(course=course)
            current_course.admins.add(admin)
            return HttpResponseRedirect('/add_professor?submitted=True')
    else:
        form = RegistryForm
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'add_professor.html', {'form':form, 'submitted':submitted})

def view_courses(request):
    course_list = Course.objects.all()

    return render(request,'view_courses.html', {'course_list': course_list})

def create_assessment(request):
    submitted = False
    users = SiteUsers.objects.all()
    teams = Team.objects.all()
    assessment = Cassess.objects.all()
    submission = Submission.objects.all()

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

def view_assessment(request, assessment):
    '''Grab all assessments, questions, responses'''
    person = request.user
    user = SiteUsers.objects.get(user =person)
    team = Team.objects.all()
    for t in team:
        for users in t.memebers.all():
            if users == user:
                team = t
    assess = Cassess.objects.get(assess_number = assessment)
    course = Course.objects.all()
    reg = Registry.objects.all()
    question = Question.objects.all()
    mc = MCResponse.objects.all()
    oe = Response.objects.all()
    test = SiteUsers.objects.all()
    submitted = False
    submission = Submission()

    if request.method == "POST":
        respondee = request.POST["reviewee"]
        test = SiteUsers.objects.get(id = respondee)
        submission.reviewee = test
        for q in question:
            if q.assessment == assess:
                submission.assessment = assess
                submission.course = assess.course
                submission.user = user
                submission.save()
                for b in mc:
                    if b.question == q and b.mc == '':
                        instance = MCResponse(question = q, mc = request.POST['mc'], responder = user)
                        instance.save()
                        submission.answerMC.add(instance)

                for c in oe:
                    if c.question == q and c.response == '':
                        inst=Response(question = q, response = request.POST['response'], responder = user)
                        inst.save()
                        submission.answer.add(inst)
        submission.save()
        return HttpResponseRedirect('/Dashboards/studashboard')

    else:
        forma = MCResponseForm
        formb = ResponseForm
        formc = SubmissionForm
        formd = CourseForm
        if 'submitted' in request.GET:
            submitted = True

    return render(request, 'view_assessment.html', {'assessment': assessment, 'assess': assess, 'course': course, 'user':user, 'question':question, 'team': team, 'mc': mc, 'oe': oe, 'forma':forma, 'formb':formb, 'formc': formc, 'formd':formd, 'submitted':submitted})

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

def view_responses(request, assessment):
    courses = Course.objects.filter(admins__username__icontains=request.user)
    course_submissions = []
    assess = Cassess.objects.get(assess_number = assessment)
    questions = Question.objects.all()
    mc = MCResponse.objects.all()
    submission = Submission.objects.all()
    response = Response.objects.all()
    for course in courses:
        submissions = Submission.objects.filter(course__course__icontains=course)
        for sub in submissions:
            course_submissions.append(sub)


    return render(request, 'view_responses.html', {'submissions': course_submissions, 'submission':submission, 'assess': assess, 'questions':questions, 'response': response, 'mc': mc})

'''def submission_deadline():
    students = SiteUsers.objects.all()
    team = Team.objects.all()
    person = request.user
    cassess = Cassess.objects.all()
    for c in cassess:
        for t in team:
            if t.course == c.course:
                date = c.due_date
                if date - timedelta(hours = 24) == datetime.now():
                    for p in t.memebers.all()
                        subject = "You have 24 hours left to answer assessment"
                        message = ''
                        email_from = settings.EMAIL_HOST_USER
                        recipient_list = {p.email,}
                        html_message = loader.render_to_string(
                            'email1.html',
                        {
                        'context':'values',
                        }
                    )

                    send_mail(subject, message, email_from, recipient_list, html_message = html_message)'''

def view_your_assessment(request, assessment):
    courses = Course.objects.all()
    team = Team.objects.all()
    person = request.user
    users = SiteUsers.objects.get(user=person)
    assess = Cassess.objects.get(assess_number = assessment)
    response = Response.objects.all()
    mc = MCResponse.objects.all()
    submission = Submission.objects.all()
    cassess = Cassess.objects.all()
    count = 0
    total = 0
    avg = 0

    for s in submission:
        if s.reviewee == users:
            if assess.course == s.course:
                for answerMC in s.answerMC.all():
                    if s.assessment == assess:
                        count = count +1
                        total = total + int(answerMC.mc)
                        avg = total / count
    return render(request, 'view_your_assessment.html', { 'assess': assess, 'assessment': assessment, 'cassess': cassess, 'team': team, 'avg':avg, 'response': response, 'mc': mc, 'cassess': cassess, 'courses:':courses, 'users': users, 'submission': submission})

def pickAssessment(request):
    assess = Cassess.objects.all()
    course = Course.objects.all()
    person = request.user
    users = SiteUsers.objects.get(user=person)
    registry = Registry.objects.all()
    return render(request, 'pickAssessment.html', {'assess': assess, 'course:':course, 'users': users, 'registry': registry})

def enroll(request):
    submitted = False
    message = 'Enrollment successful.'
    if request.method == 'POST':
        form = EnrollForm(request.POST)
        if form.is_valid():
            access_code = form.cleaned_data.get('access_code')
            course = Course.objects.get(access_code=access_code)
            if (course):
                student = SiteUsers.objects.get(user=request.user)
                course.students.add(student)
                message = 'Enrollment successful.'

            else:
                message = 'Enrollment failed. Please try again.'
        return HttpResponseRedirect('/enroll?submitted=True')
    else:
        form = EnrollForm()
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'enroll.html',  {'form': form, 'message': message, 'submitted': submitted})
