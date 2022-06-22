from django.forms.models import model_to_dict
from django.contrib.auth.hashers import make_password, check_password
from .serializer import *
from .models import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from django.contrib.auth.models import User
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import permissions
from rest_framework.decorators import api_view, permission_classes


class ListUsers(APIView):
    """
    View to list all users in the system.

    * Requires token authentication.
    * Only admin users are able to access this view.
    """
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, format=None):
       user = User.objects.all()
       serializer = UserSerializer(user,many=True)
       return Response({'payload':serializer.data})

class CustomAuthToken(ObtainAuthToken):

    def authenticate(self, request, username=None, password=None, **kwargs):
        UserModel = get_user_model()
        try:
            user = UserModel.objects.get(email=username)
        except UserModel.DoesNotExist:
            return None
        else:
            if user.check_password(password):
                return user
        return None

@api_view(['POST'])
@permission_classes((permissions.AllowAny,))
def userCreate(request):
        serializer = UserSerializer(data = request.data)
        if not serializer.is_valid():
            print(serializer.errors)
            return Response({'status':403,'errors':serializer.errors,'message':"something is wrong"})
        serializer.save()
        return Response({'status':200,'payload':serializer.data,'message':"your data save successfully"})
    

class Projects(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self,request):
        project_obj = Project.objects.all()
        serializer = ProjectSerializer(project_obj,many=True)
        return Response({'payload':serializer.data})

    def post(self,request):
        data = request.data.dict()
        data['user_id']= request.user.id
        serializer = ProjectSerializer(data = data)
        
        
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
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
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
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
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
        data = request.data.dict()
        data['user_id']= request.user.id
        serializer = TaskSerializer(data = data)
        
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
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
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
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
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
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self,request):
        columnAttribute_obj = ColumnAttribute.objects.all()
        serializer = ColumnAttributeSerializer(columnAttribute_obj,many=True)
        return Response({'payload':serializer.data})

    def post(self,request):
        data = request.data.dict()
        data['user_id']= request.user.id
        serializer = ColumnAttributeSerializer(data = data)

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
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
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
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self,request):
        comment_obj = Comment.objects.all()
        serializer = CommentSerializer(comment_obj,many=True)
        return Response({'payload':serializer.data})

    def post(self,request):
        data = request.data.dict()
        data['user_id']= request.user.id
        serializer = CommentSerializer(data = data)

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


class Permissions(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self,request):
        permission_obj = Permission.objects.all()
        serializer = PermissionSerializer(permission_obj,many=True)
        return Response({'payload':serializer.data})

    def post(self,request):
        data = request.data.dict()
        data['user_id']= request.user.id
        serializer = PermissionSerializer(data = data)

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


