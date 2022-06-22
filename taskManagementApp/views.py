
from functools import partial
from requests import request
from .serializer import *
from .models import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from django.contrib.auth.models import User
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
# from rest_framework.response import Response
# from rest_framework.authentication import TokenAuthentication
# from rest_framework.permissions import IsAuthenticated
from django.forms.models import model_to_dict

class ListUsers(APIView):
    """
    View to list all users in the system.

    * Requires token authentication.
    * Only admin users are able to access this view.
    """
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, format=None):
        """
        Return a list of all users.
        """
        user = User.objects.all()
        serializer = UserSerializer(user,many=True)
        return Response({
            'payload':serializer.data,
            'success': True
            })

class CustomAuthToken(ObtainAuthToken):

    def post(self, request):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email
        })

class Projects(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self,request):
        project_obj = Project.objects.all()
        serializer = ProjectSerializer(project_obj,many=True)
        return Response({'payload':serializer.data})

    def post(self,request):
        serializer = ProjectSerializer(data = request.data)

        if not serializer.is_valid():
            print(serializer.errors)
            return Response({'status':403,'errors':serializer.errors,'message':"something is wrong"})

        serializer.save()
        return Response({'status':200,'payload':serializer.data,'message':"your data save successfully"})
    
    def put(self,request,pk):
            project = Project.objects.get(id=pk)
            serializer = ProjectSerializer(instance=project, data = request.data)

            if not serializer.is_valid():
                print(serializer.errors)
                return Response({'status':403,'errors':serializer.errors,'message':"something is wrong"})

            serializer.save()
            return Response({'status':200,'payload':serializer.data,'message':"your data update successfully"})
    
    def patch(self,request,pk):
            # user = User.objects.get(id=request.user.id)
            project = Project.objects.get(id=pk)
            serializer = ProjectSerializer(instance=project, data = request.data,partial=True)

            if not serializer.is_valid():
                print(serializer.errors)
                return Response({'status':403,'errors':serializer.errors,'message':"something is wrong"})

            serializer.save()
            return Response({'status':200,'payload':serializer.data,'message':"partial data update successfully"})


    def delete(self,request,pk):
                project = Project.objects.get(id=pk)
                project.delete()
                return Response('Item delete Successfully')


class Tags(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    def get(self,request):
        tag_objs = Tag.objects.all()
        serializer = TagSerializer(tag_objs,many=True)
        return Response({'payload':serializer.data})

    def post(self,request):
        serializer = TagSerializer(data = request.data)
        
        if not serializer.is_valid():
            print(serializer.errors)
            return Response({'status':403,'errors':serializer.errors,'message':"something is wrong"})

        serializer.save()
        return Response({'status':200,'payload':serializer.data,'message':"your data save successfully"})
    
    def put(self,request,pk):
            tag = Tag.objects.get(id=pk)
            serializer = TagSerializer(instance=tag, data = request.data)

            if not serializer.is_valid():
                print(serializer.errors)
                return Response({'status':403,'errors':serializer.errors,'message':"something is wrong"})

            serializer.save()
            return Response({'status':200,'payload':serializer.data,'message':"your data update successfully"})
    
    def patch(self,request,pk):
            # user = User.objects.get(id=request.user.id)
            tag = Tag.objects.get(id=pk)
            serializer = TagSerializer(instance=tag, data = request.data,partial=True)

            if not serializer.is_valid():
                print(serializer.errors)
                return Response({'status':403,'errors':serializer.errors,'message':"something is wrong"})

            serializer.save()
            return Response({'status':200,'payload':serializer.data,'message':"partial data update successfully"})

    
    def delete(self,request,pk):
                tag = Tag.objects.get(id=pk)
                tag.delete()
                return Response('Item delete Successfully')


class Tasks(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    
    def get(self,request,pk=None,format = None):
        id= pk
        if id is not None:
            task_objs = Task.objects.get(id=id)
            serializer = TaskSerializer(task_objs)
            return Response({'payload':serializer.data})

        task_objs = Task.objects.all()
        serializer = TaskSerializer(task_objs,many=True)
        return Response({'payload':serializer.data})


    def post(self,request):
        
        serializer = TaskSerializer(data = request.data)
        
        if not serializer.is_valid():
            print(serializer.errors)
            return Response({'status':403,'errors':serializer.errors,'message':"something is wrong"})

        serializer.save()
        return Response({'status':200,'payload':serializer.data,'message':"your data save successfully"})
    
    def put(self,request,pk):
            # user = User.objects.get(id=request.user.id)
            task = Task.objects.get(id=pk)
            serializer = TaskSerializer(instance=task, data = request.data)

            if not serializer.is_valid():
                print(serializer.errors)
                return Response({'status':403,'errors':serializer.errors,'message':"something is wrong"})

            serializer.save()
            return Response({'status':200,'payload':serializer.data,'message':"your data update successfully"})
    
    def patch(self,request,pk):#user assign
            # user = User.objects.get(id=request.user.id)
            task = Task.objects.get(id=pk)
            serializer = TaskSerializer(instance=task, data = request.data,partial=True)

            if not serializer.is_valid():
                print(serializer.errors)
                return Response({'status':403,'errors':serializer.errors,'message':"something is wrong"})

            serializer.save()
            return Response({'status':200,'payload':serializer.data,'message':"partial data update successfully"})

    def delete(self,request,pk):
                task = Task.objects.get(id=pk)
                task.delete()
                return Response('Item delete Successfully')    



class TaskTags(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    def get(self,request):
        taskTag_obj = TaskTag.objects.all()
        serializer = TaskTagSerializer(taskTag_obj,many=True)
        return Response({'payload':serializer.data})

    def post(self,request):
        serializer = TaskTagSerializer(data = request.data)

        if not serializer.is_valid():
            print(serializer.errors)
            return Response({'status':403,'errors':serializer.errors,'message':"something is wrong"})

        serializer.save()
        return Response({'status':200,'payload':serializer.data,'message':"your data save successfully"})
    
    def put(self,request,pk):
            taskTag = TaskTag.objects.get(id=pk)
            serializer = TaskTagSerializer(instance=taskTag, data = request.data)

            if not serializer.is_valid():
                print(serializer.errors)
                return Response({'status':403,'errors':serializer.errors,'message':"something is wrong"})

            serializer.save()
            return Response({'status':200,'payload':serializer.data,'message':"your data update successfully"})
    
    def patch(self,request,pk):
            # user = User.objects.get(id=request.user.id)
            taskTag = TaskTag.objects.get(id=pk)
            serializer = TaskTagSerializer(instance=taskTag, data = request.data,partial=True)

            if not serializer.is_valid():
                print(serializer.errors)
                return Response({'status':403,'errors':serializer.errors,'message':"something is wrong"})

            serializer.save()
            return Response({'status':200,'payload':serializer.data,'message':"partial data update successfully"})

    def delete(self,request,pk):
                taskTag = TaskTag.objects.get(id=pk)
                taskTag.delete()
                return Response('Item delete Successfully')


class TaskAttributes(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    def get(self,request):
        taskAttribute_obj = TaskAttribute.objects.all()
        serializer = TaskAttributeSerializer(taskAttribute_obj,many=True)
        return Response({'payload':serializer.data})

    def post(self,request):
        serializer = TaskAttributeSerializer(data = request.data)

        if not serializer.is_valid():
            print(serializer.errors)
            return Response({'status':403,'errors':serializer.errors,'message':"something is wrong"})

        serializer.save()
        return Response({'status':200,'payload':serializer.data,'message':"your data save successfully"})
    
    def put(self,request,pk):
            taskAttribute = TaskAttribute.objects.get(id=pk)
            serializer = TaskAttributeSerializer(instance=taskAttribute, data = request.data)

            if not serializer.is_valid():
                print(serializer.errors)
                return Response({'status':403,'errors':serializer.errors,'message':"something is wrong"})

            serializer.save()
            return Response({'status':200,'payload':serializer.data,'message':"your data update successfully"})
    
    def patch(self,request,pk):
            # user = User.objects.get(id=request.user.id)
            taskAttribute = TaskAttribute.objects.get(id=pk)
            serializer = TaskAttributeSerializer(instance=taskAttribute, data = request.data,partial=True)

            if not serializer.is_valid():
                print(serializer.errors)
                return Response({'status':403,'errors':serializer.errors,'message':"something is wrong"})

            serializer.save()
            return Response({'status':200,'payload':serializer.data,'message':"partial data update successfully"})


    def delete(self,request,pk):
                taskAttribute = TaskAttribute.objects.get(id=pk)
                taskAttribute.delete()
                return Response('Item delete Successfully')


class ColumnAttributes(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    def get(self,request):
        columnAttribute_obj = ColumnAttribute.objects.all()
        serializer = ColumnAttributeSerializer(columnAttribute_obj,many=True)
        return Response({'payload':serializer.data})

    def post(self,request):
        serializer = ColumnAttributeSerializer(data = request.data)

        if not serializer.is_valid():
            print(serializer.errors)
            return Response({'status':403,'errors':serializer.errors,'message':"something is wrong"})
        
        serializer.save()
        return Response({'status':200,'payload':serializer.data,'message':"your data save successfully"})
    
    def put(self,request,pk):
            columnAttribute = ColumnAttribute.objects.get(id=pk)
            serializer = ColumnAttributeSerializer(instance=columnAttribute, data = request.data)

            if not serializer.is_valid():
                print(serializer.errors)
                return Response({'status':403,'errors':serializer.errors,'message':"something is wrong"})

            serializer.save()
            return Response({'status':200,'payload':serializer.data,'message':"your data update successfully"})
    def patch(self,request,pk):
            # user = User.objects.get(id=request.user.id)
            columnAttribute = ColumnAttribute.objects.get(id=pk)
            serializer = ColumnAttributeSerializer(instance=columnAttribute, data = request.data,partial=True)

            if not serializer.is_valid():
                print(serializer.errors)
                return Response({'status':403,'errors':serializer.errors,'message':"something is wrong"})

            serializer.save()
            return Response({'status':200,'payload':serializer.data,'message':"partial data update successfully"})


    def delete(self,request,pk):
                columnAttribute = ColumnAttribute.objects.get(id=pk)
                columnAttribute.delete()
                return Response('Item delete Successfully')


class CustomColumnValues(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    def get(self,request):
        customColumnValue_obj = CustomColumnValue.objects.all()
        serializer = CustomColumnValueSerializer(customColumnValue_obj,many=True)
        return Response({'payload':serializer.data})

    def post(self,request):
        serializer = CustomColumnValueSerializer(data = request.data)

        if not serializer.is_valid():
            print(serializer.errors)
            return Response({'status':403,'errors':serializer.errors,'message':"something is wrong"})

        serializer.save()
        return Response({'status':200,'payload':serializer.data,'message':"your data save successfully"})
    
    def put(self,request,pk):
            customColumnValue = CustomColumnValue.objects.get(id=pk)
            serializer = CustomColumnValueSerializer(instance=customColumnValue, data = request.data)

            if not serializer.is_valid():
                print(serializer.errors)
                return Response({'status':403,'errors':serializer.errors,'message':"something is wrong"})

            serializer.save()
            return Response({'status':200,'payload':serializer.data,'message':"your data update successfully"})
    def patch(self,request,pk):
            # user = User.objects.get(id=request.user.id)
            customColumnValue = CustomColumnValue.objects.get(id=pk)
            serializer = CustomColumnValueSerializer(instance=customColumnValue, data = request.data,partial=True)

            if not serializer.is_valid():
                print(serializer.errors)
                return Response({'status':403,'errors':serializer.errors,'message':"something is wrong"})

            serializer.save()
            return Response({'status':200,'payload':serializer.data,'message':"partial data update successfully"})


    def delete(self,request,pk):
                customColumnValue = CustomColumnValue.objects.get(id=pk)
                customColumnValue.delete()
                return Response('Item delete Successfully')


class Comments(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    def get(self,request):
        comment_obj = Comment.objects.all()
        serializer = CommentSerializer(comment_obj,many=True)
        return Response({'payload':serializer.data})

    def post(self,request):
        serializer = CommentSerializer(data = request.data)

        if not serializer.is_valid():
            print(serializer.errors)
            return Response({'status':403,'errors':serializer.errors,'message':"something is wrong"})

        serializer.save()
        return Response({'status':200,'payload':serializer.data,'message':"your data save successfully"})
    
    def put(self,request,pk):
            comment = Comment.objects.get(id=pk)
            serializer = CommentSerializer(instance=comment, data = request.data)

            if not serializer.is_valid():
                print(serializer.errors)
                return Response({'status':403,'errors':serializer.errors,'message':"something is wrong"})

            serializer.save()
            return Response({'status':200,'payload':serializer.data,'message':"your data update successfully"})
    
    def patch(self,request,pk):
            # user = User.objects.get(id=request.user.id)
            comment = Comment.objects.get(id=pk)
            serializer = CommentSerializer(instance=comment, data = request.data,partial=True)

            if not serializer.is_valid():
                print(serializer.errors)
                return Response({'status':403,'errors':serializer.errors,'message':"something is wrong"})

            serializer.save()
            return Response({'status':200,'payload':serializer.data,'message':"partial data update successfully"})


    def delete(self,request,pk):
                comment = Comment.objects.get(id=pk)
                comment.delete()
                return Response('Item delete Successfully')

class Permissions(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    def get(self,request):
        permission_obj = Permission.objects.all()
        serializer = PermissionSerializer(permission_obj,many=True)
        return Response({'payload':serializer.data})

    def post(self,request):
        serializer = PermissionSerializer(data = request.data)

        if not serializer.is_valid():
            print(serializer.errors)
            return Response({'status':403,'errors':serializer.errors,'message':"something is wrong"})

        serializer.save()
        return Response({'status':200,'payload':serializer.data,'message':"your data save successfully"})
    
    def put(self,request,pk):
            permission = Permission.objects.get(id=pk)
            serializer = PermissionSerializer(instance=permission, data = request.data)

            if not serializer.is_valid():
                print(serializer.errors)
                return Response({'status':403,'errors':serializer.errors,'message':"something is wrong"})

            serializer.save()
            return Response({'status':200,'payload':serializer.data,'message':"your data update successfully"})
    
    def patch(self,request,pk):
            # user = User.objects.get(id=request.user.id)
            permission = Permission.objects.get(id=pk)
            serializer = PermissionSerializer(instance=permission, data = request.data,partial=True)

            if not serializer.is_valid():
                print(serializer.errors)
                return Response({'status':403,'errors':serializer.errors,'message':"something is wrong"})

            serializer.save()
            return Response({'status':200,'payload':serializer.data,'message':"partial data update successfully"})


