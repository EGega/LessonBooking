from django.db import models

from django.contrib.auth.models import User

class Profile(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  display_name = models.CharField(max_length=40, blank=True, null=True)
  avatar = models.ImageField(upload_to='userImgs', default="avatar.png")

  def __str__(self):
    return self.user.username
