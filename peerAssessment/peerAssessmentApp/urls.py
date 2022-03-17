from django.urls import path
from . import views

app_name = 'peerAssessmentApp'

urlpatterns = [
    path('',views.signup, name='signup'), 

]