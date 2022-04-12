from django.urls import path
from . import views

app_name = 'peerAssessmentApp'

urlpatterns = [
    path('', views.home_view, name= 'home'),
    path('createuser', views.createUser, name='createuser'),
    path('about/',views.about, name = 'about'),
    path('contact/',views.contact, name = 'contact'),
    path('home/',views.home_view, name= 'home'),
    path('signup/',views.signup, name='signup'),
    path('Dashboards/studashboard/', views.studashboard, name='dashboard_s'),
    path('student_or_professor/', views.student_or_professor, name= 'student_or_professor'),
    path('Dashboards/prodashboard/', views.prodashboard, name='dashboard_p'),
    path('Dashboards/', views.my_redirect, name='dashboards'),
    path('add_course/', views.add_course, name= 'add_course'),
    path('add_professor/', views.add_professor, name= 'add_professor'),
    path('view_courses/', views.view_courses, name= 'view_courses'),
    path('create_assessment/', views.create_assessment, name= 'create_assessment'),
    path('add_teams/', views.add_teams, name= 'add_teams'),
    path('add_questions/', views.add_questions, name= 'add_questions'),
    path('choose_response/', views.choose_response, name= 'choose_response'),
    path('mc_response/', views.mc_response, name= 'mc_response'),
    path('oe_response/', views.oe_response, name= 'oe_response'),
    path('view_assessment/', views.view_assessment, name= 'view_assessment'),
]
