from django.contrib import admin
from .models import User,Skill,Student,Employee,Instructor,Interest,Profile,JobPosting
# Register your models here.
admin.site.register([User,Skill,Student,Employee,Instructor,Interest,Profile,JobPosting])