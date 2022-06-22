from django.db import models
import shortuuid
# Create your models here.
from django.db import models
from datetime import datetime
from django.contrib.auth import get_user_model
User = get_user_model()
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User



s=shortuuid.ShortUUID(alphabet="0123456789")
uid = s.random(length=5)

# Create your models here.
class Project(models.Model):
    id = models.AutoField
    project_name = models.CharField(max_length=122)
    project_description = models.TextField(null=True)
    project_id = models.SlugField(max_length=5,default=uid,unique=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.project_name

class Tag(models.Model):
    id = models.AutoField
    tag_name = models.CharField(max_length=122)
    project_id = models.ForeignKey('Project', on_delete=models.CASCADE,null=True)  # foregin key
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.tag_name


class Task(models.Model):
    id = models.AutoField
    task_title = models.CharField(max_length=122)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE,null=True)  # foregin key
    tag_id = models.ForeignKey('Tag', on_delete=models.CASCADE,null=True)  # foregin key
    project_id = models.ForeignKey('Project', on_delete=models.CASCADE,null=True)  # foregin key
    status_id = models.IntegerField(null=True)
    file_name = models.CharField(max_length=122,null=True)
    task_description = models.TextField(null=True)
    task_id = models.SlugField(max_length=6,default=uid,unique=True)
    start_date = models.DateField()
    end_date = models.DateField()   
    close_date = models.DateField(null=True)
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.task_title

class TaskTag(models.Model):
    id = models.AutoField
    task_id = models.ForeignKey('Task', on_delete=models.CASCADE,null=True)
    tag_id = models.ForeignKey('Tag', on_delete=models.CASCADE,null=True)
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

class TaskAttribute(models.Model):
    id = models.AutoField
    task_id = models.ForeignKey('Task', on_delete=models.CASCADE,null=True)
    key = models.CharField(max_length=122)
    value = models.CharField(max_length=122)
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    def __str__(self):
        return self.value


class ColumnAttribute(models.Model):
    id = models.AutoField
    user_id = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    attribute_name = models.CharField(max_length=122)
    date = models.DateTimeField(default=datetime.now())
    unique_random_id = models.SlugField(max_length=6,default=uid,unique=True)
    tag_id = models.ForeignKey('Tag', on_delete=models.CASCADE,null=True)
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.attribute_name

class CustomColumnValue(models.Model):
    id = models.AutoField
    value = models.CharField(max_length=122)
    custom_col_id = models.IntegerField()
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    def __str__(self):
        return self.value

class Comment(models.Model):
    id = models.AutoField
    task_id = models.ForeignKey('Task', on_delete=models.CASCADE,null=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    comment = models.CharField(max_length=122)
    parent_id = models.CharField(max_length=122,null=True)
    file_name = models.CharField(max_length=122,null=True)
    date_time = models.DateTimeField(default=datetime.now())
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.comment

class Permission(models.Model):
    id = models.AutoField
    user_id = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    permissions = models.CharField(max_length=255)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)\



