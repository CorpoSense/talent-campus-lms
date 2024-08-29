from django.contrib.auth.models import Group, User
from rest_framework import serializers
from .models import Course

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class CourseSerializer(serializers.ModelSerializer):
    instructor = UserSerializer(read_only=True)
    user_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Course
        fields = [
            'id', 'title', 'description', 'createdAt', 'categories',
            'rating', 'instructor', 'user_id'
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
        representation['title'] = instance.get_title_display()
        representation['description'] = instance.get_description_display()
        representation['status'] = instance.get_status_display()
        return representation