from .models import User
from rest_framework.views import APIView
from .serializers import UserSerializer
from rest_framework import generics,permissions
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from django.contrib.auth import authenticate
# Create your views here.

class RegisterUserView(APIView):
    serializer_class = UserSerializer
    permission_classes=[permissions.AllowAny]


class LoginUserView(APIView):
    authentication_classes=[TokenAuthentication]
    def post(self,request):
        user = authenticate(email = request.data["email"],password=request.data["password"])
        if(user):
            token,created = Token.objects.get_or_create(user=user)
            return Response({
                "userId" : user.id,
                "token":token
            })
        else :
            return Response({
                "error":True,"message":"Invalid Credentials"
            })