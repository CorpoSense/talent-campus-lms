from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Instructor, CourseCategorie, Course

admin.site.register(Instructor)
admin.site.register(CourseCategorie)
admin.site.register(Course)