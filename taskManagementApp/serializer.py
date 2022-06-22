from dataclasses import field
import email
from .models import *
from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework import serializers


User.email = models.EmailField(("email address"), blank=True, null=True, unique=True)


class UserSerializer(serializers.ModelSerializer):

    def validate_email(self, value):
        lower_email = value.lower()
        if User.objects.filter(email__iexact=lower_email).exists():
            raise serializers.ValidationError("Email already exists.")
        return lower_email
    class Meta:
        model = User
        fields = ('username','first_name','last_name','email','password')

    def create(self, validated_data):
        user = User(
            username=validated_data['username'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            email=validated_data['email'],
        )
        
        user.set_password(validated_data['password'])
        user.save()
        return user

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'is_active', 'id']

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = "__all__"


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = "__all__"


class TaskTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskTag
        fields = "__all__"


class ColumnAttributeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ColumnAttribute
        fields = "__all__"


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project 
        fields = ['id','project_name','project_description','project_id','user_id']


class CustomColumnValueSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomColumnValue
        fields = "__all__"


class PermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permission
        fields = "__all__"


class TaskAttributeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskAttribute
        fields = "__all__"
