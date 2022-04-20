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
    types = models.CharField(max_length=3, choices=TYPE_CHOICES, unique=False, null=True, blank=True, default=None)
    def __str__(self):
        return str(self.user)
    email = models.EmailField(max_length = 50, null = True)


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
    course_id = models.CharField(max_length = 8, primary_key = True)
    year = models.CharField(max_length = 4, null = True)
    semester = models.CharField(max_length = 6, null = True)
    admins = models.ManyToManyField(User, related_name='admins', blank=True)
    students = models.ManyToManyField(SiteUsers, related_name='students', blank=True)
    access_code = models.CharField(max_length = 5, blank = True, null = True)

    def __str__(self):
        return str(self.course)


## Registry To link the Professor to Courses
class Registry(models.Model):
    admin = models.ForeignKey(User, on_delete = models.CASCADE)
    course = models.ForeignKey(Course, on_delete = models.CASCADE)

    def __str__(self):
       return str(self.admin) + ': '  + str(self.course)

## Enrollment to link the Student/SiteUsers to Courses
# class Enrollment(models.Model):
#     SiteUser = models.ForeignKey(SiteUsers, on_delete = models.CASCADE)
#     course = models.ForeignKey(Course, on_delete = models.CASCADE)

#     def __str__(self):
#        return str(self.SiteUser) + ': '  + str(self.course)
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
    due_date= models.DateField(max_length = 1, null = True)
    publish_date = models.DateField(max_length = 1, null = True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, default = 3)

    def __str__(self):
        return str(self.assess_number)


class Question(models.Model):
    assessment = models.ForeignKey(Cassess, on_delete=models.CASCADE)
    question = models.CharField(max_length = 1000, null = True)
    def __str__(self):
        return str(self.question)
class MCResponse(models.Model):
    OPTIONS = {
        ("1", "Strongly Disagree"),
        ("2", "Disagree"),
        ("3", "Neutral"),
        ("4", "Agree"),
        ("5", "Strongly Agree"),
    }
    mc = models.CharField(max_length = 20, choices = OPTIONS, blank = True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    responder = models.ForeignKey(SiteUsers, on_delete= models.CASCADE, null = True)



    def __str__(self):
        return str(self.responder) + ": " + str(self.question)

class Response(models.Model):
    response = models.CharField( max_length= 255, blank = True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    responder = models.ForeignKey(SiteUsers, on_delete= models.CASCADE, null = True)

    def __str__(self):
        return str(self.responder) + ": " + str(self.question)

class Submission(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    assessment = models.ForeignKey(Cassess, on_delete =models.CASCADE)
    user = models.ForeignKey(SiteUsers, on_delete= models.CASCADE)
    answer = models.ManyToManyField(Response)
    answerMC = models.ManyToManyField(MCResponse)
    satus = models.CharField(max_length = 255, blank = True)
    reviewee = models.ForeignKey(SiteUsers, on_delete = models.CASCADE, related_name = "reviewer", default= None, blank=True, null=True)

    def __str__(self):
        return str(self.id)
