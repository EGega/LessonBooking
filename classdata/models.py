from django.db import models
from django.contrib.postgres.fields import ArrayField
# Create your models here.



class Teachers(models.Model):
  STARS = (
  (1, 1),
  (2, 2),
  (3, 3),
  (4, 4),
  (5, 5)
)
  first_name = models.CharField(max_length=40)
  middle_name = models.CharField(max_length=40, blank=True, null=True)
  last_name = models.CharField(max_length=40)
  profile_photo = models.ImageField(upload_to='teacherImgs', blank=True) #temporary blank true but I need to change with the final version
  introduction_video = models.FileField(upload_to='teacherIntroVid', blank=True)
  certificates = models.FileField(upload_to = 'certificates', blank=True)
  description = models.TextField()
  teacher_nationality = models.CharField(max_length=40) #this field will be visible only for staff users and can not be edited by teachers themselves
  teacher_review = models.TextField()
  teacher_stars = models.IntegerField(choices=STARS, default=5)



class Students(models.Model):
  first_name = models.CharField(max_length=40)
  last_name = models.CharField(max_length=40)
  profile_photo = models.ImageField(upload_to='studentImgs', blank=True, null=True) #temporary blank true but I need to change with the final version
  after_lesson_comments = ArrayField(models.TextField())