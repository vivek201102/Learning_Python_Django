from distutils.command.upload import upload
from django.db import models
from karamel.models import UserInfo
# Create your models here.
class Userprofile(models.Model):
    userinfo = models.ForeignKey(UserInfo, on_delete=models.CASCADE)
    status = models.CharField(max_length=50)
    bio = models.TextField()
    pic = models.ImageField(upload_to = "profiles")
