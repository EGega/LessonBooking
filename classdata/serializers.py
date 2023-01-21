from rest_framework import serializers
from .models import Teachers, Students

class TeacherSerializers(serializers.ModelSerializer):
  class Meta:
    model = Teachers
    fields = "__all__"

    
class StudentSerializers(serializers.ModelSerializer):
  class Meta:
    model = Students
    fields = "__all__"