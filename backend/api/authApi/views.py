from .models import User,Student,Skill,Interest,Employee,Instructor
from rest_framework.views import APIView
from django.contrib import messages
from django.shortcuts import redirect
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import ValidationError,AuthenticationFailed
from rest_framework_simplejwt.tokens import RefreshToken
import json
from rest_framework_simplejwt.tokens import AccessToken
from rest_framework_simplejwt.exceptions import InvalidToken, TokenError
from django.contrib.auth.tokens import default_token_generator
from django.urls import reverse_lazy
from rest_framework.response import Response
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
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from rest_framework.permissions import AllowAny
#import json
class RegisterUserView(APIView):
    #permission_classes=[AllowAny]
    def post(self,request):
        # Basic validation for required fields
        required_fields = ["type", "username", "email", "password", "firstName", "lastName","industry_name"]
        missing_fields = [field for field in required_fields if not request.data.get(field)]
        
        if missing_fields:
            return Response({
                "error": True,
                "message": f"Missing fields: {', '.join(missing_fields)}"
            }, status=400)
        userType = request.data['type']
        existingStd = User.objects.filter(email=request.data["email"]).exists()
        if(existingStd):
                raise ValidationError({
                    "error":True
                })
        

         # Additional validation based on user type
        if userType == "student" or userType == "employee":
            # Check if skills and interests are provided
            if not request.data.get("skills") or not request.data.get("interests"):
                return Response({
                    "error": True,
                    "message": "Skills and interests are required for students and employees"
                }, status=400)
    
        user = User.objects.create(email = request.data["email"],username = request.data["username"],password=request.data["password"])
        # setup profile information 
        if(request.data["type"]):
            user.type = request.data["type"]
        user.save()
        profile = user.profile 
        profile.firstName = request.data["firstName"]
        profile.lastName = request.data["lastName"]
        profile.save()
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
                #learner_group= Group.objects.get(name="Learner")
                #user.groups.add(learner_group)
            student.save()
                #print(student)
            return Response({
                "success": True,"message":"student created successufully"
            },status=201)
        elif(request.data["type"]=="employee") :
            ## case Employee 
            employee_skills=request.data["skills"]
            employee_interets=request.data["interests"]
            #emp_jobPosting = request.data["job"]
            employee = Employee.objects.create(user=user,industry = request.data["industry_name"])
            #job_posting = JobApplication.objects.create(employee=employee,title=emp_jobPosting["title"],description=emp_jobPosting["description"],
             #                                      experience=emp_jobPosting["experience"],companyName=emp_jobPosting["companyName"],
                  #                                     date_posed=emp_jobPosting["date_posed"],region=emp_jobPosting["region"],
                   #                                    contract=emp_jobPosting["contract"],industry=emp_jobPosting["industry"])
                #for lang in emp_jobPosting["languages"]:
                 #   langue,created= Language.objects.get_or_create(language=lang)
                  #  job_posting.languages.add(langue)
                   # job_posting.save()
        
                # handle skills 
            for skill_data in employee_skills:
                #print(skill_data)
                skill,created = Skill.objects.get_or_create(name = skill_data)
                employee.skills.add(skill)

            for interest_data in employee_interets:
                #print(skill_data)
                ineterst,created = Interest.objects.get_or_create(interest = interest_data)                    
                employee.interests.add(ineterst)
                #user.groups.add(learner_group)
            employee.save()
            return Response({
                "success": True,"message":"Employee created successufuly"
            },status=201)
        else : 
            # Instructor
            instructor = Instructor.objects.create(user = user,industry=request.data["industry_name"])                # add permission to instructor 
            #instructor_group = Group.objects.get(name="Instructor")
            #user.groups.add(instructor_group)
            instructor.save()
            return Response({    
                "success":True,
                "message":"Instructor created successufully"
            },status=201)



class LoginUserView(APIView):
    #authentication_classes=[TokenAuthentication]
    def authenticateUser(self,email,password):
        try:
            user = User.objects.get(email = email)
            print(user.pk)
        except User.DoesNotExist:
            raise ValidationError("User not found")
        if(user.password == password):
            return user
        else:
            raise ValidationError("invalid password !")
        
    def post(self,request):
        # Basic validation for required fields
        required_fields = ["email", "password"]
        missing_fields = [field for field in required_fields if not request.data.get(field)]
        
        if missing_fields:
            return Response({
                "error": True,
                "message": f"Missing fields: {', '.join(missing_fields)}"
            }, status=400)
        try:
            user = self.authenticateUser(email = request.data.get("email"),password=request.data.get("password"))
        except ValidationError as e:
            return Response({
                "error": True,
                "message": "invalid credentials"
            }, status=400)
        #print(request.data.get("username"),request.data.get("password"))
        #print("user is ",user.password,user.pk)
        if(user):
            #userDic = json.
            #userToDic = json.loads(user)
            refresh = RefreshToken.for_user(user=user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
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
        print(email,domain)
        existUser = User.objects.get(email=email)
        print(existUser)
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
        #print(existUser.email,subject,email_content)
        try:
            send_mail(subject, email_content, EMAIL_HOST_USER, [existUser.email], fail_silently=False)
        except Exception as e:
            print(f"Error sending email: {e}")
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


class ProfileView(APIView):
    def get(self,request,user_id):
        # get request headers 
        try:
            authorized = validToken(request.headers.get("Authorization"),user_id)
        except ValueError as e:
            return Response({
                "error":True,
                "message":str(e)
            },status=401)
        try:
            user= User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return Response({
                "error":True,
                "message":"profile doesn't exist"
            })
        # get the profile 
        profile = user.profile 
        #print("here",user.profile)
        # prepare the data 
         # Prepare the response data
        data = {}
        if(user.type == "student"):
            data = {
                "user_id": user.id,
                "email": user.email,
                "username": user.username,
                "first_name": profile.firstName,
                "last_name": profile.lastName,
                "phone_number": profile.phoneNumber,
                "sexe": profile.sexe,
                "type": user.type,
                "skills":list(user.student.skills.values("id","name")),
                "interests":list(user.student.interests.values("id","interest"))
            }
        elif(user.type == "employee"):
            data = {
                "user_id": user.id,
                "email": user.email,
                "username": user.username,
                "first_name": profile.firstName,
                "last_name": profile.lastName,
                "phone_number": profile.phoneNumber,
                "sexe": profile.sexe,
                "type": user.type,
                "skills":user.employee.skills,
                "interests":user.employee.interests,
                "job_posting_info":user.employee.job_posting
            }
        else:
            data={
                 "user_id": user.id,
                "email": user.email,
                "username": user.username,
                "first_name": profile.firstName,
                "last_name": profile.lastName,
                "phone_number": profile.phoneNumber,
                "sexe": profile.sexe,
                "type": user.type,
            }
        return Response(data)
    def put(self,request,user_id):
        try:
            authorized = validToken(request.headers.get("Authorization"),user_id)
        except ValueError as e:
            return Response({
                "error":True,
                "message":str(e)
            },status=401)
        try:
            user = User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return Response({
                "error" : True,
                "message":"User doesn't exist"
            })
        # get profile to update 
        profile = user.profile
        # get request body 
        body = request.data
        profile.firstName = body.get("first_name",profile.firstName) ## default value in case first_name absent
        profile.lastName = body.get("last_name",profile.lastName) ## default value in case last name not provided
        profile.sexe = body.get("sexe",profile.sexe)
        profile.phoneNumber = body.get("phone_number",profile.phoneNumber)
        profile.save()

        if(user.type == "student" or user.type == "employee"):
            if(user.type=="student"):
                user.student.industry=body.get("industry_name",user.student.industry)
            else :
                user.employee.industry=body.get("industry_name",user.employee.industry)
            # skills 
            skills = body.get("skills",[])
            user.student.skills.set([])
            if(len(skills)!=0):
                for skill in skills:
                    sk,created = Skill.objects.get_or_create(name = skill)
                    user.student.skills.add(sk)
            #interests
            interests = body.get("interests",[])
            user.student.interests.set([])
            if(len(interests)!=0):
                for interest in interests:
                    it,created = Interest.objects.get_or_create(interest = interest)
                    user.student.interests.add(it)
            if(user.type == "student"):
                user.student.save()
            else:
                user.employee.save()
        return Response({
            "success":True,
            "message":"Profile updated successfully"
        })

## refersh token view 
class RefreshTokenView(APIView):
    @csrf_exempt
    def post(self, request,user_id):
        refresh_token = request.data.get("refreshToken")

        if not refresh_token or not user_id:
            return Response({
                "error": True,
                "message": "Missing refresh token or user ID."
            }, status=400)

        try:
            # Verify if the user exists
            user = User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return Response({
                "error": True,
                "message": "User not found."
            }, status=status.HTTP_404_NOT_FOUND)

        try:
            # Decode the refresh token
            token = RefreshToken(refresh_token)

            # Verify if the refresh token is valid for the given user
            if str(token.get("user_id")) != str(user_id):
                return Response({
                    "error": True,
                    "message": "Token does not belong to the given user."
                }, status=401)

            # Generate a new access token
            new_access_token = str(token.access_token)

            return Response({
                "success": True,
                "accessToken": new_access_token
            }, status=200)

        except TokenError as e:
            return Response({
                "error": True,
                "message": "Invalid refresh token."
            }, status=401)
        

def validToken(token,userId):
    if not token:
        raise ValueError('Authorization header is missing.')
    try:
        token_str = token.split(' ')[1]
        accessToken = AccessToken(token_str)
        if(str(accessToken.get("user_id")) != str(userId)):
            raise ValueError("unauthorized action")
        return True  # Token is valid
    except (IndexError, InvalidToken, TokenError):
        raise ValueError('Invalid or expired token.')