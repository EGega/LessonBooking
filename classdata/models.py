from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.contrib.auth.models import User
# Create your models here.



class Teachers(models.Model):
  STARS = (
  (5, "5"),
  (4, "4"),
  (3, "3"),
  (2, "2"),
  (1, "1"),
  
)
  
  first_name = models.CharField(max_length=40)
  middle_name = models.CharField(max_length=40, blank=True, null=True)
  last_name = models.CharField(max_length=40)
  profile_photo = models.ImageField(upload_to='teacherImgs', blank=True) #temporary blank true but I need to change with the final version
  introduction_video = models.FileField(upload_to='teacherIntroVid', blank=True)
  certificates = models.FileField(upload_to = 'certificates', blank=True)
  description = models.TextField()
  teacher_nationality = models.CharField(max_length=40, null=True) #this field will be visible only for staff users and can not be edited by teachers themselves
  teacher_review = models.TextField()
  teacher_stars = models.IntegerField(choices=STARS, default=5)

  def __str__(self):
    return f'{self.first_name} {self.last_name}'



class Students(models.Model):
  first_name = models.CharField(max_length=40)
  last_name = models.CharField(max_length=40)
  profile_photo = models.ImageField(upload_to='studentImgs', blank=True, null=True) #temporary blank true but I need to change with the final version
  after_lesson_comments = ArrayField(models.TextField(), null=True)
  teachers = models.ManyToManyField(Teachers, related_name="teachers",)
  def __str__(self):
    return f'{self.first_name} {self.last_name}'



class Lessons(models.Model):
  user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
  # teacher = models.ForeignKey(Teachers, related_name="teachers", on_delete=models.CASCADE)
  # student = models.ForeignKey(Students, related_name="students", on_delete=models.CASCADE)