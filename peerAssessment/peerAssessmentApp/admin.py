from django.contrib import admin
from .models import SiteUsers, Course, Registry, Team, Question, Assessment, Answer, Submission, Choice

# Register your models here.

admin.site.register(SiteUsers)
admin.site.register(Course)
admin.site.register(Registry)
# admin.site.register(Enrollment)
admin.site.register(Team)
admin.site.register(Assessment)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(Submission)
admin.site.register(Choice)
# admin.site.register(Cassess)
# admin.site.register(Question)
# admin.site.register(Response)
# admin.site.register(MCResponse)