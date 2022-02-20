from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class UserInfo(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=255)
    mobile = PhoneNumberField()
    gender = models.CharField(max_length=50)
    dob = models.DateField()
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=200)

    