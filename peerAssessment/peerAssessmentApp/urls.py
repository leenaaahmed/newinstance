from django.urls import path
from . import views

app_name = 'peerAssessmentApp'

urlpatterns = [
    path('home/',views.home_view, name= 'home'),
    path('signup/',views.signup, name='signup')
]