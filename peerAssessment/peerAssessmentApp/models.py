from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class SiteUsers(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, related_name = 'siteusers')
    date_of_birth = models.DateField()
    TYPE_CHOICES = (
        ('pro', 'professor'),
        ('stu', 'student'),
        )
    type = models.CharField(max_length=3, choices=TYPE_CHOICES, unique=True, null=True, blank=True, default=None)
    def __str__(self):
        return str(self.user)


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

    def __str__(self):
        return str(self.course)


## Registry To link the Professor to Courses
class Registry(models.Model):
    User = models.ForeignKey(User, on_delete = models.CASCADE)
    course = models.ForeignKey(Course, on_delete = models.CASCADE)
    
    def __str__(self):
       return str(self.User) + ': '  + str(self.course)

## Enrollment to link the Student/SiteUsers to Courses
class Enrollment(models.Model):
    SiteUser = models.ForeignKey(SiteUsers, on_delete = models.CASCADE)
    course = models.ForeignKey(Course, on_delete = models.CASCADE)

    def __str__(self):
       return str(self.SiteUser) + ': '  + str(self.course)
    #group_name = models.CharField(max_length = 10, null = True)

## Team models for associating Siteusers into teams
class Team(models.Model):
    team_name = models.CharField(max_length = 40, null = True)
    course = models.ForeignKey(Course, on_delete = models.CASCADE, null = True)
    memebers =  models.ManyToManyField(SiteUsers)

    def __str__(self):
        return str(self.course) + ",  Team: " + str(self.team_name)

##Cassess object
class Cassess(models.Model):
    assess_number = models.CharField(max_length = 6, null = True)
    due_date= models.CharField(max_length = 1, null = True)
    publish_date = models.CharField(max_length = 1, null = True)
    question = models.CharField(max_length = 1000, null = True)
    question_format = models.CharField(max_length = 5, null = True)

    def __str__(self):
        return str(self.User) + str(self.Cassess)
