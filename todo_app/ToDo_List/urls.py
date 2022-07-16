from django.urls import path
from . views import *
urlpatterns=[
    path('list/',ToDoList.as_view()),
    path('create/',ToDoCreate.as_view()),
    path('details/<int:pk>',ToDoDetail.as_view())
]