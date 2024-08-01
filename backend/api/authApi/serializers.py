from .models import User
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=["email","username","password"]
        extra_kwargs={"password":{
            "write_only": True
        }}
    def create(self,validatedData):
        user = User.objects.create_user(**validatedData)
        return user