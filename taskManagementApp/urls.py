from . import views
from django.urls import path, include
# from rest_framework import routers
from .views import *

# router = routers.DefaultRouter()
# router.register('tasks', viewset=views.TaskList)
# router.register('tags', viewset=views.TagList)
# router.register('taskTags', viewset=views.TaskTagList)
# router.register('ColumnAttributes', viewset=views.ColumnAttributeList)
# router.register('comments', viewset=views.CommentList)
# router.register('projects', viewset=views.ProjectList)
# router.register('customColumnValues', viewset=views.CustomColumnValueList)
# router.register('permission', viewset=views.PermissionList)
# router.register('taskAttribute', viewset=views.TaskAttributeList)


urlpatterns = [
    # path('', include(router.urls)),
    #To user list:response users list
    path('api/users/',ListUsers.as_view()),

    #To view tokens: response user_id,token and email
    path('api/token/auth/', CustomAuthToken.as_view()),

    #Projects related routes
    path('project/',Projects.as_view()),
    path('project/<str:pk>/',Projects.as_view()),

    #Tag related route
    path('tag/',Tags.as_view()),
    path('tag/<str:pk>/',Tags.as_view()),

    # Task related routes
    path('task/',Tasks.as_view()),
    path('task/<str:pk>/',Tasks.as_view()),


    #TaskTags related routes
    path('tasktag/',TaskTags.as_view()),
    path('tasktag/<str:pk>/',TaskTags.as_view()),

    #TaskAttributes related routes
    path('taskAttribute/',TaskAttributes.as_view()),
    path('taskAttribute/<str:pk>/',TaskAttributes.as_view()),

    #ColumnAttribute related routes
    path('columnattribute/',ColumnAttributes.as_view()),
    path('columnattribute/<str:pk>/',ColumnAttributes.as_view()),
    
    #CustomColumnValue related routes
    path('customColumnValue/',CustomColumnValues.as_view()),
    path('customColumnValue/<str:pk>/',CustomColumnValues.as_view()),

    #Comment related routes
    path('comment/',Comments.as_view()),
    path('comment/<str:pk>/',Comments.as_view()),

   
    #Permissions related routes
    path('permission/',Permissions.as_view()),
    path('permission/<str:pk>/',Permissions.as_view()),
   
]
