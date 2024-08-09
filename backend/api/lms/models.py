from django.db import models
from authApi.models import Instructor,Student,Employee,User
import enum
# Create your models here.


class CourseCategorie(models.Model):
    categorieName = models.CharField(max_length=100)


class Course(models.Model):
    title = models.CharField()
    desc = models.TextField()
    instructor = models.ForeignKey(Instructor,on_delete=models.CASCADE,related_name="courses")
    categories = models.ManyToManyField(CourseCategorie,related_name="courses")
    rating = models.FloatField(default=1.0)

class Video(models.Model):
    url = models.URLField()
    title = models.CharField()
    description = models.TextField()
    course= models.ForeignKey(Course,on_delete=models.CASCADE,related_name="videos")


class Enrollement(models.Model):
    student = models.ForeignKey(Student,on_delete=models.CASCADE,related_name="myEnrollements",null=True,blank=True)
    course= models.ForeignKey(Course,on_delete=models.CASCADE,related_name="enrolled_students")
    employee = models.ForeignKey(Employee,on_delete=models.CASCADE,related_name="enrolled_employees",null=True,blank=True)
    startedAt = models.DateField()
    progress = models.IntegerField()

    def save(self, *args, **kwargs):
        if self.student is None and self.employee is None:
            raise ValueError("An enrollment must have either a student or an employee.")
        if self.student is not None and self.employee is not None:
            raise ValueError("An enrollment can only have either a student or an employee, not both.")
        super().save(*args, **kwargs)
    

class Recommendation(models.Model):
    course = models.ForeignKey(Course,on_delete=models.CASCADE,related_name="recommendations")
    student=models.ManyToManyField(Student,related_name="my_recommendations")
    degree = models.IntegerField()


class Review(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name="MyReviews")
    course= models.ForeignKey(Course,on_delete=models.CASCADE,related_name="course_reviews")
    comment = models.TextField()
    rating = models.IntegerField()

class quizType(enum.Enum):
    MULTIPLECHOICES="multiple choices"
    QA= "qa"

class Quiz(models.Model):
    course = models.ForeignKey(Course,on_delete=models.CASCADE,related_name="quizzes")
    question=models.TextField()
    quiztype = models.CharField(max_length=20,choices=[(tag,tag.value) for tag in quizType])
    #answer= models.TextField(null=True)

class QuizChoice(models.Model):
    quiz = models.ForeignKey(Quiz,on_delete=models.CASCADE,related_name="quiz")
    content = models.CharField()
    isCorrect= models.BooleanField(default=False)

class QA(models.Model):
    quiz = models.ForeignKey(Quiz,on_delete=models.CASCADE,related_name="quiz")
    answer = models.TextField()
    explanation = models.TextField()

class Subscription(models.Model):
    student= models.ForeignKey(Student,on_delete=models.CASCADE,related_name="student")
    employee= models.ForeignKey(Employee,on_delete=models.CASCADE,related_name="employee")
    course = models.ForeignKey(Course,on_delete=models.CASCADE,related_name="course")
    createdAt = models.DateTimeField(auto_now=True)
    amount = models.IntegerField()

