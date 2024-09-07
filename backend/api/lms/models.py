from django.db import models
from authApi.models import User,Student,Employee,Skill,Language,Instructor,IndustryChoices
import enum
# Create your models here.


class CourseCategorie(models.Model):
    categorieName = models.CharField(max_length=100)

class Course(models.Model):
    title = models.CharField(max_length=100)
    desc = models.TextField(max_length=300)
    image = models.TextField(max_length=1000)
    instructor = models.ForeignKey(Instructor,on_delete=models.CASCADE,related_name="courses")
    categories = models.ManyToManyField(CourseCategorie,related_name="courses")
    rating = models.FloatField(default=1.0)

class Video(models.Model):
    url = models.URLField()
    title = models.CharField(max_length=100)
    description = models.TextField()
    course= models.ForeignKey(Course,on_delete=models.CASCADE,related_name="videos")


class Enrollement(models.Model):
    student = models.ForeignKey(Student,on_delete=models.CASCADE,related_name="myEnrollements",null=True,blank=True)
    course= models.ForeignKey(Course,on_delete=models.CASCADE,related_name="enrolled_students")
    employee = models.ForeignKey(Employee,on_delete=models.CASCADE,related_name="enrolled_employees",null=True,blank=True)
    startedAt = models.DateField(auto_now=True)

    def save(self, *args, **kwargs):
        if self.student is None and self.employee is None:
            raise ValueError("An enrollment must have either a student or an employee.")
        if self.student is not None and self.employee is not None:
            raise ValueError("An enrollment can only have either a student or an employee, not both.")
        super().save(*args, **kwargs)
    
class Discussion(models.Model):
    course=models.ForeignKey(Course,on_delete=models.CASCADE,related_name="discussions")
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name="my_discussions")
    title = models.TextField(null=False)
    discussion_content = models.TextField(default="")
    createdAt = models.DateTimeField(auto_now_add=True)

class DiscussionComment(models.Model):
    discussion=models.ForeignKey(Discussion,on_delete=models.CASCADE,related_name="comments")
    created_at = models.DateTimeField(auto_now_add=True)
    content = models.TextField(null=False)
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name="my_comments")

class AssessmentType(models.Model):
    type_name = models.CharField(max_length=100)

#An assessment could consist of multiple quizzes or just be a larger form of a quiz.

    

class UserProgress(models.Model):
    #user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='progress')
    enrollement = models.ForeignKey(Enrollement, on_delete=models.CASCADE, related_name='user_progresses',default=None)
    progress_percentage = models.FloatField()
    last_accessed = models.DateTimeField(auto_now=True)

class ContractTypes(enum.Enum):
    PARTTIME="part time"
    FULLTIME="full time"
    FREELANCECONTRACT="Freelance Contract"
    FIXEDTERM="Fixed-term"

class JobPosting(models.Model):
    #employee = models.ForeignKey(Employee,on_delete=models.CASCADE,related_name="job_posting")
    title = models.CharField(max_length=50)
    description= models.TextField()
    companyName = models.CharField(max_length=255)
    region = models.CharField(max_length=255)
    #experience = models.TextField()
    employementType=models.CharField(max_length=255)
    salaryRange = models.FloatField()
    date_posed = models.DateField(auto_now_add=True)
    contract=models.CharField(max_length=50,choices=[(tag,tag.value) for tag in ContractTypes])
    requiredSkills=models.ManyToManyField(Skill,related_name="job_required_skills")
    preferredSkills=models.ManyToManyField(Skill,related_name="job_preferred_skills")
    industry= models.CharField(max_length=100,choices=[(tag,tag.value) for tag in IndustryChoices])
    languages = models.ManyToManyField(Language,related_name="related_jobs")


class JobApplication(models.Model):
    job_posting = models.ForeignKey(JobPosting,on_delete=models.CASCADE,related_name="job_applications")
    employee = models.ForeignKey(Employee,on_delete=models.CASCADE,related_name="my_job_applications")
    status=models.CharField(max_length=55,choices=[("pending","PENDING"),("hired","HIRED"),("rejected","REJECTED")])
    motif = models.TextField(null=False)


class SkillMatch(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='skill_matches')
    job_posting = models.ForeignKey(JobPosting, on_delete=models.CASCADE, related_name='skill_matches')
    match_percentage = models.FloatField()


class Recommendation(models.Model):
    student = models.ForeignKey(Student,on_delete=models.CASCADE,related_name="my_recommendations",null=True,blank=True)
    employee=models.ManyToManyField(Employee,related_name="my_recommendations",null=True,blank=True)
    degree = models.IntegerField()
    recommendationType=models.CharField(max_length=100,choices=[("course","COURSE"),("job","JOB")],default="course")

    def save(self, *args, **kwargs):
        if self.student is None and self.employee is None:
            raise ValueError("An enrollment must have either a student or an employee.")
        if self.student is not None and self.employee is not None:
            raise ValueError("An enrollment can only have either a student or an employee, not both.")
        super().save(*args, **kwargs)

class CourseRecommendation(models.Model):
    course = models.ForeignKey(Course,on_delete=models.CASCADE,related_name="recommended_to")
    recommendation = models.ForeignKey(Recommendation,on_delete=models.CASCADE,related_name="course_recommendation")


class CareerRecommendation(models.Model):
    jobPosting = models.ForeignKey(JobPosting,on_delete=models.CASCADE,related_name="recommended_to")
    createdAt = models.DateTimeField(auto_now_add=True)
    relevanceScore = models.FloatField()
    recommendation = models.ForeignKey(Recommendation,on_delete=models.CASCADE,related_name="career_recommendation")


class Review(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name="MyReviews")
    course= models.ForeignKey(Course,on_delete=models.CASCADE,related_name="course_reviews")
    comment = models.TextField()
    rating = models.FloatField()



class questionType(enum.Enum):
    MULTIPLECHOICES="multiple choices"
    QA= "qa"

class QuestionChoice(models.Model):
    #question = models.ManyToManyField(Question,related_name="question_choices")
    content = models.CharField(max_length=255)
    isCorrect= models.BooleanField(default=False)

class QA(models.Model):
    #question = models.ManyToManyField(Question,related_name="qa_question")
    answer = models.TextField()
    explanation = models.TextField()

class Question(models.Model):
    #quiz=models.ManyToManyField(Quiz,related_name="questions")
    text = models.TextField(null=False)
    questionType=models.CharField(max_length=50,choices=[(tag,tag.value) for tag in questionType])
    choices = models.ManyToManyField(QuestionChoice,related_name="question_choices")
    qas=models.ManyToManyField(QA,related_name="qa_questions")
class Quiz(models.Model):
    course = models.ForeignKey(Course,on_delete=models.CASCADE,related_name="quizzes")
    title=models.TextField()
    createdAt = models.DateTimeField(auto_now_add=True)
    createdBy= models.ForeignKey(Instructor,on_delete=models.CASCADE,related_name="myQuestions")
    questions = models.ManyToManyField(Question,related_name="quiz_questions")
    #quiztype = models.CharField(max_length=20,choices=[(tag,tag.value) for tag in quizType])
    #answer= models.TextField(null=True)

class Assessment(models.Model):
    course = models.ForeignKey(Course,on_delete=models.CASCADE,related_name="course_assessements")
    title = models.TextField(null=False)
    description = models.TextField(null=False)
    assessementType=models.ForeignKey(AssessmentType,on_delete=models.CASCADE,related_name="assessements")
    createdAt = models.DateTimeField(auto_now_add=True)
    quizzes = models.ManyToManyField(Quiz,related_name="assessements")

class AssessementSubmission(models.Model):
    assessement = models.ForeignKey(Assessment,on_delete=models.CASCADE,related_name="sumissions")
    score = models.FloatField()
    submittedAt = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name="my_submissions")


class UserQuizSubmission(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='quiz_submissions')
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='submissions')
    submitted_at = models.DateTimeField(auto_now_add=True)
    score = models.FloatField(default=0.0)

    def __str__(self):
        return f"{self.user.username}'s submission for {self.quiz.title}"


class Subscription(models.Model):
    student= models.ForeignKey(Student,on_delete=models.CASCADE,related_name="student")
    employee= models.ForeignKey(Employee,on_delete=models.CASCADE,related_name="employee")
    course = models.ForeignKey(Course,on_delete=models.CASCADE,related_name="course")
    createdAt = models.DateTimeField(auto_now=True)
    amount = models.IntegerField()

