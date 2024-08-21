from django.contrib import admin
from .models import CourseCategorie,Course,Video,Enrollement,Recommendation,CourseRecommendation,CareerRecommendation,AssessementSubmission,Assessment,Discussion,DiscussionComment,JobPosting,JobApplication,UserProgress,AssessmentType,SkillMatch, Review,Quiz,QuizChoice,QA,Subscription


admin.site.register([CourseCategorie,Course,Video,Enrollement,Recommendation,Review,Quiz,QuizChoice,QA,Subscription,CourseRecommendation,CareerRecommendation,AssessementSubmission,Assessment,AssessmentType,Discussion,DiscussionComment,JobPosting,JobApplication,UserProgress,SkillMatch])

# Register your models here.
