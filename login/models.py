from django.db import models

# Create your models here.

class UserInfo(models.Model):
    user = models.CharField(max_length=3)
    passwd = models.CharField(max_length=3)
