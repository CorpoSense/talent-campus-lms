from django.db import models
from django.contrib.auth.models import AbstractUser,Group,Permission
import enum
# Create your models here.

class userType(enum.Enum):
    STUDENT = "student"
    EMPLOYEE = "employee"
    INSTRUCTOR = "instructor"
    ADMIN = "Admin"

class User(AbstractUser):
    email = models.EmailField(blank=False)
    username= models.CharField(blank=False,max_length=40)
    type=models.CharField(max_length=40,choices=[(tag,tag.value) for tag in userType])
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

class Language(enum.Enum):
    ARABIC="arabic"
    FRENCH="français"
    ENGLISH="english"


class Student(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    skills = models.ManyToManyField(Skill,related_name="std_skills")
    interests = models.ManyToManyField(Interest,related_name="std_interests")
    industry = models.CharField(max_length=255,choices=IndustryChoices)

class Employee(models.Model):
    user= models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    skills = models.ManyToManyField(Skill,related_name="emp_skills")
    interests = models.ManyToManyField(Interest,related_name="emp_interests")
    industry = models.CharField(max_length=255,choices=IndustryChoices)

class Instructor(models.Model):
    user= models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    industry = models.CharField(max_length=255,choices=IndustryChoices)

class sexeEnum(enum.Enum):
    MALE="MALE"
    FEMALE="FEMALE"

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    firstName = models.CharField(max_length=50,blank=True)
    lastName = models.CharField(max_length=50,blank=True)
    phoneNumber = models.CharField(max_length=255)
    sexe= models.CharField(max_length=6,choices=[(tag,tag.value) for tag in sexeEnum ])

class ContractTypes(enum.Enum):
    PARTTIME="part time"
    FULLTIME="full time"
    FREELANCECONTRACT="Freelance Contract"
    FIXEDTERM="Fixed-term"

class JobPosting(models.Model):
    employee = models.ForeignKey(Employee,on_delete=models.CASCADE,related_name="job_posting")
    title = models.CharField(max_length=50)
    description= models.TextField()
    companyName = models.CharField(max_length=255)
    region = models.CharField(max_length=255)
    experience = models.TextField()
    date_posed = models.DateField()
    contract=models.CharField(max_length=50,choices=[(tag,tag.value) for tag in ContractTypes])
    skillCategory=models.ManyToManyField(Skill,related_name="job_skills")
    industry= models.CharField(max_length=100,choices=[(tag,tag.value) for tag in IndustryChoices])
    languages = models.CharField(max_length=20,choices=[(tag,tag.value) for tag in Language])

