from django.http import Http404
from django.shortcuts import render
from rest_framework import generics, status, mixins
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics

from .serializer import ToDoserializer
from .models import ToDo

# Create your views here.

           ### Using generics class_based view ###

class ToDoList(generics.ListAPIView):
    queryset = ToDo.objects.all()
    serializer_class = ToDoserializer
class ToDoCreate(generics.CreateAPIView):
    queryset = ToDo.objects.all()
    serializer_class = ToDoserializer
class ToDoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ToDo.objects.all()
    serializer_class = ToDoserializer



         ### using class-based views ###
# class ToDoList(APIView):
#     def get(self, request, format=None):
#         snippets = ToDo.objects.all()
#         serializer = ToDoserializer(snippets, many=True)
#         return Response(serializer.data)
#
#     def post(self, request, format=None):
#         serializer = ToDoserializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
# class ToDoDetail(APIView):
#
#     def get_object(self, pk):
#         try:
#             return ToDo.objects.get(pk=pk)
#         except ToDo.DoesNotExist:
#             raise Http404
#
#     def get(self, request, pk):
#         snippet = self.get_object(pk)
#         serializer = ToDoserializer(snippet)
#         return Response(serializer.data)
#
#     def put(self, request, pk):
#         snippet = self.get_object(pk)
#         serializer = ToDoserializer(snippet, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def delete(self, request, pk):
#         snippet = self.get_object(pk)
#         snippet.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


            #### Using mixin ###

# class ToDoList(mixins.ListModelMixin,generics.GenericAPIView):
#     queryset = ToDo.objects.all()
#     serializer_class =ToDoserializer
#     def list(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)
#
# class ToDoDetail(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,generics.GenericAPIView):
#     queryset = ToDo.objects.all()
#     serializer_class =ToDoserializer
#
#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)
#
#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)
#
#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)