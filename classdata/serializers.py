from rest_framework import serializers
from .models import Teachers, Students, Lessons

class TeacherSerializers(serializers.ModelSerializer):
  class Meta:
    model = Teachers
    fields = "__all__"

    
# class StudentSerializers(serializers.ModelSerializer):
#   # teacher = serializers.StringRelatedField()
#   class Meta:
#     model = Students
#     fields = "__all__"

class StudentSerializers(serializers.ModelSerializer):
    teachers = serializers.PrimaryKeyRelatedField(many=True, queryset=Teachers.objects.all())
    class Meta:
        model = Students
        fields = ('id', 'first_name', 'last_name', 'profile_photo', 'after_lesson_comments', 'teachers')



class LessonSerializers(serializers.ModelSerializer):
  # teacher = TeacherSerializers(required=True) 
  class Meta:
    model = Lessons
    fields = "__all__"