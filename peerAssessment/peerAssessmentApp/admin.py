from django.contrib import admin
from .models import SiteUsers, Course, Registry, Enrollment, Team, Cassess

# Register your models here.

admin.site.register(SiteUsers)
admin.site.register(Course)
admin.site.register(Registry)
admin.site.register(Enrollment)
admin.site.register(Team)
admin.site.register(Cassess)