from rest_framework.response import Response
from rest_framework.views import APIView
from authApi.models import User
from django.views import View
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
import json
from .models import CourseCategorie,Course,Video,Enrollement,UserProgress
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

@method_decorator(csrf_exempt, name='dispatch')
class CourseView(APIView):
    def post(self,request):
        data=json.loads(request.body)
        print(data)
        if(not data.get("instructor_id")):
            return Response({
                "error":True,
                "message":"missing instructor id"
            })
        try:
            instructor = User.objects.get(pk=data.get("instructor_id"))
            print(instructor)
        except User.DoesNotExist:
            return Response({
                "error":True,
                "message":"invalid instructor id"
            })
        course_name = data.get("course_name")
        course_description=data.get("course_descr")
        course_categories=data.get("course_categories")
        course_videos = data.get("video_links")

        if(not course_name or not course_description or not len(course_categories) or not len(course_videos)):
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
        course.save()
        return Response({
            "success":True,
            "message":"course has been created successufuly"
        })
    


class CourseViewDetails(APIView):
    def get(self,request,course_id):
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
        print(course.videos)
        data_to_return = {
            "course_id" :course.pk,
            "course_title" : course.title,
            "course_description" : course.desc,
            "course_categories": list(course.categories.values("categorieName")),
            "course_videos" : list(course.videos.values("id","url","title","description")),
            "course_instructor" :  {
                "id":course.instructor.user.pk,
                "username":course.instructor.user.username,
                "firstName":course.instructor.user.profile.firstName,
                "lastName":course.instructor.user.profile.lastName
            }
        }
        return Response(data=data_to_return,status=200)
        
class CourseUpdateView(APIView):
    def put(self,request,course_id):
        try:
            existingCourse = Course.objects.get(pk=course_id)
        except Course.DoesNotExist:
            return Response({"error":True,"message":"course not found"},status=400)
        data = json.loads(request.body)
        print(data.get("videos"))
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
        print("hello world")
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
        user = get_object_or_404(User, pk=user_id)
        if(user.type == "student"):
            ## create enrollment 
            enrollement = Enrollement.objects.create(course=course,student=user.student)
            UserProgress.objects.create(enrollement=enrollement,progress_percentage=0.0)
        if(user.type == "employee"):
            ## create enrollment 
            enrollement = Enrollement.objects.create(course=course,student=user.employee)
            UserProgress.objects.create(enrollement=enrollement,progress_percentage=0.0)
        return Response({
            "success":True,
            "message": "Student enrolled successfully"
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
        print(user.type)
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

        print(data)
        if not len(data):
            return Response({"message":"no enrolled courses for now"})
        return Response(data,status=200)