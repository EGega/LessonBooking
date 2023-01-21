# from django.shortcuts import render
from rest_framework import viewsets
from .serializers import TeacherSerializers
from .models import Teachers


class TeacherView(viewsets.ModelViewSet):
  queryset = Teachers.objects.all()
  serializer_class = TeacherSerializers

# Create your views here.
