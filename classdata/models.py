from django.db import models

# Create your models here.

class Teacher(models.Model):
  first_name = models.CharField(max_length=40)
  middle_name = models.CharField(max_length=40, blank=True, null=True)
  last_name = models.CharField(max_length=40)
  profile_photo = models.ImageField(upload_to='teacherImgs', blank=True) #temporary blank true but I need to change with the final version
  introduction_video = models.FileField(upload_to='teacherIntroVid', blank=True)
  certificates = models.FileField(upload_to = 'certificates', blank=True)
  description = models.TextField()
  teacherNationality = models.CharField(max_length=40) #this field will be visible only for staff users and can not be edited by teachers themselves
