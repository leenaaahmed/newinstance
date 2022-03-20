from django.urls import path
from . import views

app_name = 'peerAssessmentApp'

urlpatterns = [
    path('createuser', views.createUser, name='createuser'),
    path('',views.signup, name='signup'),

]