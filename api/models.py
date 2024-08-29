from django.db import models
from django.contrib.auth.models import User

class Instructor(models.Model):
    user = models.OneToOneField(User,on_delete=models.RESTRICT,primary_key=True,related_name="instructor")
    createdAt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username

    class Meta:
        ordering = ['-createdAt']
    
class CourseCategorie(models.Model):
    categorieName = models.CharField(max_length=100)
    createdAt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.categorieName

    class Meta:
        ordering = ['-createdAt']


class Course(models.Model):
    STATUS_CHOICES = (
        ('draft', 'DRAFT'),
        ('published', 'PUBLISHED'),
        ('expired', 'EXPIRED'),
    )
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    image = models.CharField(max_length=200, null=True)
    instructor = models.ForeignKey(Instructor,on_delete=models.CASCADE,related_name="courses")
    categories = models.ManyToManyField(CourseCategorie,related_name="courses")
    rating = models.FloatField(default=1.0)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='draft')
    createdAt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-createdAt']
