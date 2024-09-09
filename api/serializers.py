from django.contrib.auth.models import Group, User
from rest_framework import serializers
from .models import Course

class UserSerializer(serializers.HyperlinkedModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups', 'password']
    
    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class CourseSerializer(serializers.ModelSerializer):
    # instructor = UserSerializer(read_only=True)
    user_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Course
        fields = [
            'id', 'title', 'description', 'createdAt', 'categories',
            'rating', 'image', 'user_id'
        ]
        read_only_fields = ['id', 'createdAt']

    def create(self, validated_data):
        user_id = validated_data.pop('user_id')
        instructor = User.objects.get(id=user_id)
        course = Course.objects.create(instructor=instructor, **validated_data)
        return job

    def update(self, instance, validated_data):
        user_id = validated_data.pop('user_id', None)
        if user_id:
            user = User.objects.get(id=user_id)
            instance.user = user
        return super().update(instance, validated_data)

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['title'] = instance.title
        representation['description'] = instance.description
        representation['status'] = instance.status
        return representation