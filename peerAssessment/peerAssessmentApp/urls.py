from django.urls import path
from . import views

app_name = 'peerAssessmentApp'

urlpatterns = [
    path('createuser', views.createUser, name='createuser'),
    path('home/',views.home_view, name= 'home'),
    path('signup/',views.signup, name='signup')
]