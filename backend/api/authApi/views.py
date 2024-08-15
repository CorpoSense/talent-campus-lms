from .models import User,Student,Skill,Interest,Employee,JobPosting,Instructor,Language
from rest_framework.views import APIView
from .serializers import UserSerializer
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth.tokens import default_token_generator
from django.urls import reverse_lazy
from django.http import HttpResponse
from api.settings import EMAIL_HOST_USER
from django.core.mail import send_mail,BadHeaderError
from django.contrib.auth.views import PasswordResetView
from django.contrib.auth.views import PasswordResetDoneView,PasswordResetConfirmView,PasswordResetCompleteView
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
#import json
# Create your views here.

class RegisterUserView(APIView):
    def post(self,request):
        userType = request.data['type']
        existingStd = User.objects.filter(email=request.data["email"]).exists()
        if(existingStd):
                raise ValidationError({
                    "error":True,
                    "message":"email is already linked to another account"
                })
        else:
            user = User.objects.create(email = request.data["email"],username = request.data["username"],password=request.data["password"])
            # setup profile information 
            profile = user.profile 
            profile.firstName = request.data["firstName"]
            profile.lastName = request.data["lastName"]
            #profile.phoneNumber = request.data["phoneNumber"]
            if(userType == "student"):
                #print("called from student")
                #print("hello world")
                stdSkills = request.data["skills"]
                #print(stdSkills)
                stdInterests=  request.data["interests"]
                # create student entity
                student = Student.objects.create(user=user,industry=request.data["industry_name"])

                # handle skills 
                for skill_data in stdSkills:
                    #print(skill_data)
                    skill,created = Skill.objects.get_or_create(name = skill_data)
                    student.skills.add(skill)
                for interest_data in stdInterests:
                    #print(skill_data)
                    ineterst,created = Interest.objects.get_or_create(interest = interest_data)
                    student.interests.add(ineterst)
                #print(student)
                return Response({
                    "success": True
                })
            elif(request.data["type"]=="employee") :
                ## case Employee 
                employee_skills=request.data["skills"]
                employee_interets=request.data["interests"]
                emp_jobPosting = request.data["job"]
                print(emp_jobPosting)
                employee = Employee.objects.create(user=user,industry = request.data["industry_name"])
                job_posting = JobPosting.objects.create(employee=employee,title=emp_jobPosting["title"],description=emp_jobPosting["description"],
                                                       experience=emp_jobPosting["experience"],companyName=emp_jobPosting["companyName"],
                                                       date_posed=emp_jobPosting["date_posed"],region=emp_jobPosting["region"],
                                                       contract=emp_jobPosting["contract"],industry=emp_jobPosting["industry"])
                for lang in emp_jobPosting["languages"]:
                    langue,created= Language.objects.get_or_create(language=lang)
                    job_posting.languages.add(langue)
        
                # handle skills 
                for skill_data in employee_skills:
                    #print(skill_data)
                    skill,created = Skill.objects.get_or_create(name = skill_data)
                    employee.skills.add(skill)
                for interest_data in employee_interets:
                    #print(skill_data)
                    ineterst,created = Interest.objects.get_or_create(interest = interest_data)
                    employee.interests.add(ineterst)
                return Response({
                    "success": True
                })
            else : 
                # Instructor
                instructor = Instructor.objects.create(user = user,industry=request.data["industry_name"])
                return Response({
                    "success":True
                })



class LoginUserView(APIView):
    authentication_classes=[TokenAuthentication]
    def authenticateUser(self,email,password):
        try:
            user = User.objects.get(email = email)
        except User.DoesNotExist:
            return Response({
                "error" : True,
                "message": "wrong email entered"
            })
        if(user.check_password(password)):
            return UserSerializer(user).data
        else:
            return Response({"error":True,"message":"Invalid password"})
        
    def post(self,request):
        user = self.authenticateUser(email = request.data["email"],password=request.data["password"])
        if(user):
            #userDic = json.
            #userToDic = json.loads(user)
            print(user["id"])
            token,created = Token.objects.get_or_create(user=user)
            return Response({
                "userId" : user["id"],
                "token":token
            })
        else :
            return Response({
                "error":True,"message":"Invalid Credentials"
            })
    
class GetUserProfile(APIView):
    def get(self,request,pk):
        return ""
    
class CustomPasswordResetView(PasswordResetView):
    template_name = 'reset/password_reset_form.html'
    email_template_name = 'reset/password_reset_email.html'
    subject_template_name = 'reset/password_reset_subject.txt'
    success_url = reverse_lazy('password_reset_done')

    def form_valid(self, form):
        email = form.cleaned_data['email']
        domain = self.request.headers["Host"]
        existUser = User.objects.get(email=email)
        print(existUser.pk)
        if not existUser:
            messages.error(self.request, "There is no user registered with the specified email address.")
            return self.form_invalid(form)
         #If the email exists, proceed with the standard process
        #return super().form_valid(form)
        subject = "Password Reset Requested"
        email_template_name = "reset/password_reset_subject.txt"
        c={
            "email":email,
            "domain":domain,
            "site_name":"Campus Talents",
            "uid":urlsafe_base64_encode(force_bytes(existUser.pk)),
            "user":existUser,
            "token": default_token_generator.make_token(existUser),
            "protocol":"http"
        }
        email_content = render_to_string(email_template_name,c)
        #print(email_content)
        try:
            send_mail(subject,email_content,EMAIL_HOST_USER,[existUser.email],fail_silently=False)
        except BadHeaderError:
            return HttpResponse("invalid header found.")
        return redirect("/auth/password_reset_done/")

class customResetPasswordDone(PasswordResetDoneView):
    template_name = 'reset/password_reset_done.html'
    
class customPasswordResetConfirm(PasswordResetConfirmView):
    template_name='reset/password_reset_confirm.html'
    success_url=reverse_lazy("auth/reset_done/")
    def get_user(self, uidb64):
        try:
            uid = urlsafe_base64_decode(uidb64).decode()
            return User.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            return None
    def dispatch(self, *args, **kwargs):
        user =self.get_user(kwargs["uidb64"])
        token = kwargs['token']
        print("token is ",token)
        if user is None or not self.token_generator.check_token(user, token):
            print("dkhalll")
            messages.error(self.request, "The password reset link was invalid or has expired. Please request a new one.")
            #return redirect('reset_password')
        return super().dispatch(*args, **kwargs)
    def form_valid(self, form):
        #print(form.cleaned_data)
        new_password = form.cleaned_data.get('new_password1')
        confirm_password = form.cleaned_data.get('new_password2')
        
        if new_password != confirm_password:
            form.add_error('new_password2', "Passwords do not match.")
            return self.form_invalid(form)
        user = form.save(commit=False)  # We don't save immediately, because we want to set the password first
        user.set_password(new_password)  # Set the new password
        user.save()  # Save the user with the updated password
        return redirect("/auth/reset_done/")
class customPasswordResetCompleteView(PasswordResetCompleteView):
    template_name="reset/password_reset_complete.html"


