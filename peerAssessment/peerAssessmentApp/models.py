from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class SiteUsers(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    date_of_birth = models.DateField()

'''
## Student object for db
class Student(models.Model):
    student_id = models.CharField(max_length = 8)
    first_name = models.CharField(max_length = 50)
    last_name = models.CharField(max_length = 50)
    email = models.EmailField(max_length = 50, primary_key = True)
    

## Professor object db
class Professor(models.Model):
    professor_id = models.CharField(max_length = 8)
    first_name = models.CharField(max_length = 50)
    last_name = models.CharField(max_length = 50)
    email = models.EmailField(max_length = 50, primary_key = True)

'''


## Course object
class Course(models.Model):
    course = models.CharField(max_length = 40, null = True)
    course_id = models.CharField(max_length = 10, primary_key = True)
    year = models.CharField(max_length = 4, null = True)
    semester = models.CharField(max_length = 1, null = True)

## Registry To link the Professor to Courses
class Registry(models.Model):
    User =  models.ForeignKey(User, on_delete = models.CASCADE)
    course = models.ForeignKey(Course, on_delete = models.CASCADE)

#3 Enrollment to link the Student/SiteUsers to Courses
class Enrollment(models.Model):
    SiteUser = models.ForeignKey(SiteUsers, on_delete = models.CASCADE)
    course = models.ForeignKey(Course, on_delete = models.CASCADE)