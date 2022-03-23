from django.urls import path
from . import views

app_name = 'peerAssessmentApp'

urlpatterns = [
    path('', views.signup, name= 'home'),
    path('createuser', views.createUser, name='createuser'),
    path('home/',views.home_view, name= 'home'),
    path('signup/',views.signup, name='signup'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('student_or_professor/', views.student_or_professor, name= 'student_or_professor')
]