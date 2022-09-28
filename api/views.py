from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from api.serializers import TodoSerializer
from rest_framework.response import Response
from Todoapp.models import Todo
from rest_framework import authentication,permissions
class TodosView(ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    authentication_classes = [authentication.BasicAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    def get_queryset(self):
        return Todo.objects.filter(user=self.request.user)
    # def list(self,request,*args,**kwargs):
    #     todos=Todo.objects.filter(user=True)
    #     serializer=TodoSerializer(todos,many=True)
    #     return Response(data=serializer.data)
    def create(self, request, *args, **kwargs):
        serializer=TodoSerializer(data=request.data,context={"user":request.user})
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)
