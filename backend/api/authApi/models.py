from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import AbstractUser,Group,Permission
from django.dispatch import receiver
# Create your models here.

class userType(models.TextChoices):
    STUDENT = "student"
    EMPLOYEE = "employee"
    INSTRUCTOR = "instructor"
    ADMIN = "Admin"

class User(AbstractUser):
    email = models.EmailField(blank=False)
    username= models.CharField(blank=False,max_length=40)
    type=models.CharField(max_length=40,choices=[(tag,tag.value) for tag in userType],default=userType.STUDENT)
    groups = models.ManyToManyField(Group, related_name='authApi_user_groups')
    user_permissions = models.ManyToManyField(Permission, related_name='authApi_user_permissions')

class Skill(models.Model):
    name = models.CharField(max_length=255, unique=True)

class Interest(models.Model):
    interest = models.CharField(max_length=255,unique=True)


class IndustryChoices(models.TextChoices):
    IT = 'IT', 'Information Technology'
    FINANCE = 'FIN', 'Finance'
    HEALTHCARE = 'HEALTH', 'Healthcare'
    EDUCATION = 'EDU', 'Education'
    MINING = "MINING"
    TECHNOLOGY='TECHNOLOGY'
    AGRICULTURE='AGRICULTURE'
    HOSPITALITY="HOSPITALITY INDUSTRY"
    FOODINDUSTRY='FOOD INDUSTRY'
    TRANSPORTATION='TRANSPORTATION'
    FASHION="FASHION"
    TELECOMMUNICATION="TELECOMMUNICATION"
    ProfessionalScientificTechnicalServices="Professional, Scientific and Technical Services"
    WholesaleTrade="Wholesale Trade"
    Manufacturing="Manufacturing"
    BUSINESS = "BUSINESS"
    InfrastructureANDContractors="Infrastructure and Contractors"

class Language(models.Model):
    language = models.CharField(max_length=60)


class Student(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True,related_name="student")
    skills = models.ManyToManyField(Skill,related_name="std_skills")
    interests = models.ManyToManyField(Interest,related_name="std_interests")
    industry = models.CharField(max_length=255,choices=IndustryChoices)

class Employee(models.Model):
    user= models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True,related_name="employee")
    skills = models.ManyToManyField(Skill,related_name="emp_skills")
    interests = models.ManyToManyField(Interest,related_name="emp_interests")
    industry = models.CharField(max_length=255,choices=IndustryChoices)

class Instructor(models.Model):
    user= models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True,related_name="instructor")
    industry = models.CharField(max_length=255,choices=IndustryChoices)

class sexeEnum(models.TextChoices):
    MALE="MALE"
    FEMALE="FEMALE"

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True,related_name="profile")
    firstName = models.CharField(max_length=50,blank=True)
    lastName = models.CharField(max_length=50,blank=True)
    phoneNumber = models.CharField(max_length=255)
    sexe= models.CharField(max_length=6,choices=[(tag,tag.value) for tag in sexeEnum ])

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)