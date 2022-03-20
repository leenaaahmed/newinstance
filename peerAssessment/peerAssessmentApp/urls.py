from django.urls import path
from . import views

app_name = 'peerAssessmentApp'

urlpatterns = [
    path('createuser', views.createUser, name='createuser'),
    path("login", views.login, name="login"),
    path('',views.signup, name='signup')

]