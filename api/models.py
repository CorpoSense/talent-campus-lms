from django.db import models
from django.contrib.auth.models import User

class Instructor(models.Model):
    user= models.OneToOneField(User,on_delete=models.RESTRICT,primary_key=True,related_name="instructor")
    createdAt = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-createdAt']
    
class CourseCategorie(models.Model):
    categorieName = models.CharField(max_length=100)
    createdAt = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-createdAt']


class Course(models.Model):
    STATUS_CHOICES = (
        ('draft', 0),
        ('published', 1),
        ('expired', 2),
    )
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=300)
    instructor = models.ForeignKey(Instructor,on_delete=models.CASCADE,related_name="courses")
    categories = models.ManyToManyField(CourseCategorie,related_name="courses")
    rating = models.FloatField(default=1.0)
    status = models.IntegerField(default=0, choices=STATUS_CHOICES)
    createdAt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-createdAt']
