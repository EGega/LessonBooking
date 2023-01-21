# from django.shortcuts import render
from rest_framework import viewsets
from .serializers import TeacherSerializers, StudentSerializers
from .models import Teachers, Students


class TeacherView(viewsets.ModelViewSet):
  queryset = Teachers.objects.all()
  serializer_class = TeacherSerializers

class StudentView(viewsets.ModelViewSet):
  queryset = Students.objects.all()
  serializer_class = StudentSerializers

# Create your views here.
