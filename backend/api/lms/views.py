from rest_framework.response import Response
from rest_framework.views import APIView
from authApi.models import User
from django.views import View
from django.http import JsonResponse
import json
from .models import CourseCategorie,Course,Video
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

@method_decorator(csrf_exempt, name='dispatch')
class CourseView(APIView):
    def post(self,request):
        data=json.loads(request.body)
        print(data)
        if(not data.get("instructor_id")):
            print('cammmm')
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
    