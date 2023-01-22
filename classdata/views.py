# from django.shortcuts import render
from rest_framework import viewsets
from .serializers import TeacherSerializers, StudentSerializers, LessonSerializers
from .models import Teachers, Students, Lessons


class TeacherView(viewsets.ModelViewSet):
  queryset = Teachers.objects.all()
  serializer_class = TeacherSerializers

class StudentView(viewsets.ModelViewSet):
  queryset = Students.objects.all()
  serializer_class = StudentSerializers

class LessonView(viewsets.ModelViewSet):
  queryset = Lessons.objects.all()
  serializer_class = LessonSerializers

# Create your views here.
