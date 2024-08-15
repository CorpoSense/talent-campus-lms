from .models import User
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from .utils import sendActivationEmail
from .models import Profile
from rest_framework.exceptions import ValidationError
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=["id","email","username","password","type"]
        extra_kwargs={"password":{
            "write_only": True
        }}
    def create(self,validatedData):
        print(validatedData)
        user= User.objects.filter(email = validatedData.get("email")).exists()
        # add profile 
        #profile = Profile.objects.create()
        #print(user)
        if(user):
            raise ValidationError({"error":True,"message":"user is already exist"})
        else:
            user = User.objects.create_user(**validatedData)
            sendActivationEmail(user)
            return Response({
                "success":True
            })