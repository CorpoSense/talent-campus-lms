from django.shortcuts import render
from .models import User
from .serializers import UserSerializer
from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework import generics

# Create your views here.

#create a view to add a user
# generic will do under the hood the creation of an user for us.
class createUserView(generics.CreateAPIView):
    # to make sure that will not create a user that already exist
    querySet = User.objects.all()
    # this serializer will tell this view which kind of data we accept
    serialize_class = User
    # who can call this function (view)
    permissions = [AllowAny]

