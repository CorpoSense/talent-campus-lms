from rest_framework.response import Response
from rest_framework.views import APIView
from authApi.models import User
from django.views import View
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
import json
from .models import CourseCategorie,Course,Video,Question,Assessment,Enrollement,Quiz,QA,QuestionChoice,UserProgress,Review,Discussion,DiscussionComment,AssessmentType
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.mixins import PermissionRequiredMixin
@method_decorator(csrf_exempt, name='dispatch')
class CourseView(APIView):
    #permission_required="lms.create_course"
    #raise_exception=True
    def post(self,request):
        auth_header = request.headers.get("Authorization")
        if(auth_header is None or not auth_header):
            return Response({
                "error":True,
                "message":"Unauthorized action"
            },status=401)
        data=json.loads(request.body)
        print(data)
        if(not data.get("instructor_id")):
            return Response({
                "error":True,
                "message":"missing instructor id"
            })
        try:
            instructor = User.objects.get(pk=data.get("instructor_id"))
            #print(instructor)
        except User.DoesNotExist:
            return Response({
                "error":True,
                "message":"invalid instructor id"
            })
        course_name = data.get("course_name")
        course_description=data.get("course_descr")
        course_categories=data.get("course_categories")
        course_videos = data.get("video_links")

        if((not course_name) or (not course_description) or (not len(course_categories)) or (not len(course_videos))):
            return Response({
                "error":True,
                "message":"some fields are required"
            })
        #categories
        course = Course.objects.create(desc=course_description,title=course_name,instructor=instructor.instructor)
        for category in course_categories:
            cat,created=CourseCategorie.objects.get_or_create(categorieName=category)
            course.categories.add(cat)
        #videos 
        for video_data in course_videos:
            if not video_data:
                return Response({
                    "error":True,
                    "message":"video Data is missing"
                })
            if((not video_data.get("url")) or (not video_data.get("title")) or (not video_data.get("description"))):
                print("hi from algeria")
                return Response({
                    "error":True,
                    "message":"video data are missing"
                })
            vid,created = Video.objects.get_or_create(url=video_data.get("url"),title=video_data.get("title"),description=video_data.get("description"),course=course)
            course.videos.add(vid)
        print(course.pk)
        course.save()
        return Response({
            "success":True,
            "message":"course has been created successufuly"
        })
    


class CourseViewDetails(APIView):
    def get(self,request,course_id):
        auth_header = request.headers.get("Authorization")
        if(auth_header is None or not auth_header):
            return Response({
                "error":True,
                "message":"Unauthorized action"
            },status=401)
        if(not course_id):
            return Response({
                "error":True,"message":"missing course id"
            })
        try:
            course = Course.objects.get(pk=course_id)
        except Course.DoesNotExist:
            return Response({
                "error":True,
                "message":"course not found"
            })
        #print(course.videos)
        data_to_return = {
            "course_id" :course.pk,
            "course_title" : course.title,
            "course_description" : course.desc,
            "course_categories": list(course.categories.values("categorieName")),
            #"course_videos" : list(course.videos.values("id","url","title","description")),
            "course_instructor" :  {
                "id":course.instructor.user.pk,
                "username":course.instructor.user.username,
                "firstName":course.instructor.user.profile.firstName,
                "lastName":course.instructor.user.profile.lastName
            }
        }
        return Response(data=data_to_return,status=200)
        
class CourseUpdateView(APIView):
    #permission_required="lms.change_course"
    #raise_exception=True
    def put(self,request,course_id):
        try:
            existingCourse = Course.objects.get(pk=course_id)
        except Course.DoesNotExist:
            return Response({"error":True,"message":"course not found"},status=400)
        data = json.loads(request.body)
        #print(data.get("videos"))
        existingCourse.title = data.get("title",existingCourse.title)
        existingCourse.desc= data.get("description",existingCourse.desc)

        #set videos 
        if(not len(data.get("videos"))):
            existingCourse.save()
        else:
            existingCourse.videos.set([])
            for vid in data.get("videos"):
                video,created = Video.objects.get_or_create(url=vid.get("url"),title=vid.get("title"),description=vid.get("description"),course=existingCourse)
                existingCourse.videos.add(video)
        existingCourse.save()
        return Response({
            "success":True,
            "message":"Course updated successufully"
        },status=200)


@method_decorator(csrf_exempt, name='dispatch')
class CourseDeleteView(View):
    def delete(self,request,course_id):
        #print("hello world")
        if(not course_id):
            return JsonResponse({
                "error":True,
                "message":"missing course id"
            })
        try:
            course = Course.objects.get(pk=course_id)
        except Course.DoesNotExist:
            return JsonResponse({
                "error":True,
                "message":"course not found"
            })
        course.delete()
        return JsonResponse({
            "success":True,
            "message":"course deleted successufully"
        })
    

# Enrollements

class CourseEnrollementView(APIView):
    def post(self,request,course_id):
        try:
            course = Course.objects.get(pk=course_id)
        except Course.DoesNotExist:
            return Response({
                "error":True,"message":"course not found"
            })
        data = json.loads(request.body.decode('utf-8'))
        user_id = data.get('user_id')
        if(not user_id):
            return Response({
                "error":True,
                "message":"invalid user id"
            },status=400)
        user = get_object_or_404(User, pk=user_id)
        if(user.type == "student"):
            ## create enrollment 
            enrollement = Enrollement.objects.create(course=course,student=user.student)
            UserProgress.objects.create(enrollement=enrollement,progress_percentage=0.0)
            print(enrollement.pk)
            return Response({
                "success":True,
                "message": "student enroll the course successufully"
            })
        elif(user.type == "employee"):
            ## create enrollment 
            enrollement = Enrollement.objects.create(course=course,student=user.employee)
            print(enrollement.pk)
            UserProgress.objects.create(enrollement=enrollement,progress_percentage=0.0)
            return Response({
                "success":True,
                "message": "employee enroll the course successufully"
            })
        else:
            return Response({
            "success":True,
            "message": "instructor can not enroll the course"
            })
    
    def delete(self,request,course_id):
        try:
            course = Course.objects.get(pk=course_id)
        except Course.DoesNotExist:
            return Response({
                "error":True,
                "message":"course not found"
            })
        data = json.loads(request.body.decode('utf-8'))
        user_id = data.get('user_id')
        try:
            user = get_object_or_404(User, pk=user_id)
        except User.DoesNotExist:
            return Response({
                "error":True,
                "message":"user not found"
            })
        # delete enrollement ---> delete all user progress 
        if user.type == "student":
            enrollment = Enrollement.objects.filter(course=course, student=user.student).first()
        elif user.type == "employee":
            enrollment = Enrollement.objects.filter(course=course, employee=user.employee).first()
        else:
            return Response({"error": True, "message": "Invalid user type"}, status=400)

        if enrollment:
            enrollment.delete()
            #UserProgress.objects.filter(enrollment=enrollment).delete()
            return Response({"success": True, "message": "Enrollment removed successfully"})
        else:
            return Response({"error": True, "message": "Enrollment not found"}, status=404)

    
#@login_required
@method_decorator(csrf_exempt, name='dispatch')
class GetEnrolledCoursesView(APIView):
    def post(self,request):
        body = json.loads(request.body)
        user_id = body.get("user_id")
        if(not user_id):
            return Response({
                "error":True,
                "message":"invalid user_id"
            })
        try:
            user = User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return Response({
                'error':True,
                "message":"user doesn't exist !"
            })
    # check user type :
        enrolledCourses=[]
        data = []
        if(user.type=="student"):
            enrolledCourses=user.student.myEnrollements.all()
        elif(user.type == "employee"):
            enrolledCourses= user.employee.enrolled_employees.all()
        else :
            return Response({'error':True,'message':"something went wrong"})
        print(enrolledCourses)
        data = [{
            "course_id": enroll.course.id,
            "title": enroll.course.title,
            "description": enroll.course.desc,
            "instructor": enroll.course.instructor.user.username,
            "rating":enroll.course.rating,
                } for enroll in enrolledCourses]
        if not len(data):
            return Response({"message":"no enrolled courses for now"})
        return Response(data,status=200)
    
class EnrolledCourseViewDetails(APIView):
    def get(self,request,enroll_id):
        try:
            enroll = Enrollement.objects.get(pk=enroll_id)
        except Enrollement.DoesNotExist:
            return Response({
                "error":True,
                "message":"invalid enrollementId"
            })
        #print(enroll.course.videos)
        data = {
            "enroll_id":enroll_id,
            "course_id": enroll.course.id,
            "title": enroll.course.title,
            "description": enroll.course.desc,
            "instructor": enroll.course.instructor.user.username,
            "rating":enroll.course.rating,
            "videos":[
                {
                    "url" : video.url,
                    "title":video.title,
                    "description":video.description
                } for video in enroll.course.videos.all()
            ]
            }
        return Response(data=data,status=200)


## Rating

class RatingView(APIView):
    #permission_classes=[IsAuthenticated]
    def post(self,request):
        data = json.loads(request.body)
        user_id = data.get("user_id")
        course_id = data.get("course_id")
        comment = data.get("comment")
        rating = data.get("rating")
        if((not user_id) or (not course_id) or (not comment) or(not rating)):
            return Response({
                "error":True,
                "message":"missing fields"
            })
        # check if the course already exist
        try:
            course = Course.objects.get(pk=course_id)
        except Course.DoesNotExist:
            return Response({
                "error":True,
                "message":"course not found"
            })
         # Check if the rating is valid
        if not (1 <= int(rating) <= 5):
            return Response({"error": True, "message": "Rating must be between 1 and 5"}, status=400)
        # Check if the user has already reviewed this course
        user = User.objects.get(pk=user_id)
        existing_review = Review.objects.filter(course=course, user=user).first()
        if existing_review:
            return Response({"error": True, "message": "You have already reviewed this course"}, status=400)
        
        # else we add the review 
        Review.objects.create(course=course,user=user,comment=comment,rating=rating)
        # update the global rating 
        self.update_course_rating(course=course)

        return Response({
            "success":True,
            "message":"Review added successfully"
        })

    def update_course_rating(self, course):
        reviews = course.course_reviews.all()
        total_rating = sum(review.rating for review in reviews)
        course.rating = total_rating / reviews.count()
        course.save()



## Discussions
class CreateDiscussionCourseView(APIView):
    #method : Post 
    #request paarms : course_id : Int 
    #request body : {user_id : Int,title:string,content : string}
    def post(self,request,course_id):
        auth_header = request.headers.get("Authorization")
        if(auth_header is None or not auth_header):
            return Response({
                "error":True,
                "message":"Unauthorized action"
            },status=401)
        try:
            course = Course.objects.get(pk=course_id)
        except Course.DoesNotExist:
            return Response({
                "error":True,
                "message":"course not found"
            })
        data = json.loads(request.body)
        title = data.get("title")
        content = data.get("content")
        user_id = data.get("user_id")

        if((not title) or (not content) or (not user_id)):
            return Response({
                "error":True,
                "message":"something went wrong"
            })
        user = User.objects.get(pk=user_id)
        discussion = Discussion.objects.create(course=course, user=user, title=title, discussion_content=content)
        return Response({"success": True, "message": "Discussion created successfully", "discussion_id": discussion.id})
    
class CourseDiscussionsView(APIView):
    # method == GET 
    # request params : course_id : Int
    def get(self,request,course_id):
        try:
            course = Course.objects.get(pk=course_id)
        except Course.DoesNotExist :
            return Response({
                "error":True,
                "message":"course not found"
            })
        #course = get_object_or_404(Course, pk=course_id)
        discussions = course.discussions.all()

        data = [{
            "discussion_id": discussion.id,
            "title": discussion.title,
            "content": discussion.discussion_content,
            "user": discussion.user.username,
            "created_at": discussion.createdAt,
            "comments": list(discussion.comments.values('user__username', 'content', 'created_at'))
        } for discussion in discussions]

        return Response({"course_id": course.id, "discussions": data})


class AddDiscussionCommentView(APIView):
    #permission_classes = [IsAuthenticated]
    # method : Post 
    # request body : {
    #  user_id : Int, content:string
    #}
    # params = discussion_id : Int
    def post(self, request, discussion_id):
        try:
            discussion = get_object_or_404(Discussion, pk=discussion_id)
        except Discussion.DoesNotExist:
            return Response({
                "error":True,
                "message":"discussion not found"
            })
        print("callledd")
        data = json.loads(request.body)
        userId = request.data.get("user_id")
        content = request.data.get("content")

        if not content:
            return Response({"error": True, "message": "Content is required"}, status=400)
        user = get_object_or_404(User,pk=userId)
        comment = DiscussionComment.objects.create(discussion=discussion, user=user, content=content)
        return Response({"success": True, "message": "Comment added successfully", "comment_id": comment.id})

# quizzes :
class CreateQuizView(APIView):
    #permission_classes = [IsAuthenticated]
    def post(self, request, course_id):
        try:
            ##print("called",course_id)
            course = get_object_or_404(Course, pk=course_id)
        except Course.DoesNotExist:
            return Response({
                "error":True,
                "message":"course not found"
            })
        ##print(request.data)
        instructor_id = request.data.get("instructor_id")
        title = request.data.get('title')
        questions=request.data.get("questions")
        #quizType = request.data.get("type")
        if ((not instructor_id ) or (not title) or (not len(questions))):
            return Response({
                "error":True,
                "message":"missing information !"
            },status=400)
        user = get_object_or_404(User,pk=instructor_id)
        quiz = Quiz.objects.create(course=course,title=title,createdBy=user.instructor)
        
        # loop over questions 
        for question in questions:
            if(question["questionType"]=="multiple choices"):
                ques,_=Question.objects.get_or_create(text=question.get("text"),questionType=question.get("questionType"))
                choices = question.get("choices")
                for choice in choices:
                 ch,created = QuestionChoice.objects.get_or_create(content=choice["content"],isCorrect=choice["isCorrect"])
                 ques.choices.add(ch)
                 #quiz.quiz_choices.add(ch)
            else:
                # it QA question
                qa,created=QA.objects.get_or_create(answer=question.get("answer"),explanation=question.get("explanation"))
                ques.qas.add(qa)
            #save question 
            ques.save()
            # set quiz 
            quiz.questions.add(ques)
        quiz.save()
        return Response({"message": "Quiz created successfully"},status=201)
    
class QuizDeleteView(APIView):
    def delete(self,request,quiz_id):
        try:
            quiz=Quiz.objects.get(pk=quiz_id)
        except Quiz.DoesNotExist:
            return Response({
                "error":True,
                "message":"invalid quiz id"
            })
        quiz.delete()
        return Response({
            "success":True,
            "message":"Quiz deleted successufully"
        })

class UpdateQuizView(APIView):
    def put(self,request,quiz_id):
        try:
            quiz = Quiz.objects.get(pk=quiz_id)
            print(quiz.title)
        except Quiz.DoesNotExist:
            return Response({
                "error":True,
                "message":"invalid quiz id"
            })
        
        quiz_title = request.data.get("title")
        if(quiz_title):
            quiz.title = quiz_title
        if(not len(request.data.get("questions"))):
            quiz.questions.set([])
            for ques in request.data.get("questions"):
                que,_=Question.objects.get_or_create(questionType = ques.get("questionType"),text = ques.get("text"))
                if(ques.get("questionType"=="multiple choices")):
                    choices = question.get("choices")
                    for choice in choices:
                        ch,created = QuestionChoice.objects.get_or_create(content=choice["content"],isCorrect=choice["isCorrect"])
                        que.choices.add(ch)
                else:
                    # it QA question
                    qa,_=QA.objects.get_or_create(answer=question.get("answer"),explanation=question.get("explanation"))
                    que.qas.add(qa)
                que.save()
                quiz.questions.add(que)
        quiz.save()
        return Response({
            "success":True,"message":"quiz updated usccessufully"
        })
        
        


class AssessmentView(APIView):
    #permission_classes = [IsAuthenticated]

    def post(self, request,course_id):
        try:
            course = Course.objects.get(pk=course_id)
        except Course.DoesNotExist:
            return Response({
                "error":True,
                "message":"invalid course id"
            },status=400)
        title = request.data.get('title')
        description = request.data.get('description')
        assessmentType = request.data.get("assessementType")
        quiz_ids = request.data.get('quiz_ids', [])
        # validate data
        if not title:
            return Response({"error": "Title is required"}, status=400)
        if not description:
            return Response({"error": "Description is required"}, status=400)
        if not assessmentType:
            return Response({
                "error":True,
                "message":"assessementType is required"
            })

        asseType,_ = AssessmentType.objects.get_or_create(type_name = assessmentType)
        #print(asseType)
        # Create the assessment
        assessment = Assessment.objects.create(title=title, description=description,assessementType=asseType,course=course)
        # map over quizzes 
        for quiz_id in quiz_ids:
            try:
                quiz = Quiz.objects.get(pk=quiz_id)
            except Quiz.DoesNotExist:
                return Response({
                    "error": True,
                    "message": "Invalid quiz ID"
                }, status=400)  
            assessment.quizzes.add(quiz)

        # Add quizzes to the assessment
        quizzes = Quiz.objects.filter(id__in=quiz_ids)
        assessment.quizzes.set(quizzes)

        return Response({
            "message": "Assessment created successfully",
            "assessment_id": assessment.id,
            "quizzes": [quiz.title for quiz in quizzes]
        })
    
class DeleteAssessementView(APIView):
    def delete(self,request,asse_id):
        try:
            assessement = Assessment.objects.get(pk=asse_id)
        except Assessment.DoesNotExist:
            return Response({
                "error":True,
                "message":"invalid assessement id"
            })
        assessement.delete()
        return Response({
            "success":True,
            "message":"assessement deleted successufully"
        })