from django.db import models
from django.conf import settings
import os
import uuid
import datetime 
from django.utils import timezone






def user_directory_path(request,filename):
    now_time=datetime.datetime.now().strftime("%Y%m%d%H:%M:%S")
    new_filename="%s%s"%(now_time,filename)
    return os.path.join('post/',new_filename)
# Create your models here.
class technologies(models.Model):
    name=models.CharField(max_length=100)
    icon=models.ImageField(null=True)
    def __str__(self):
        return str(self.name)


class education(models.Model):
    title=models.CharField(max_length=100)
    companyname=models.CharField(max_length=100)
    icon=models.ImageField(null=True)
    date=models.CharField(max_length=100)
    description=models.TextField(max_length=500)
    def __str__(self):
        return str(self.title)


class experiences(models.Model):
    title=models.CharField(max_length=100)
    companyname=models.CharField(max_length=100)
    icon=models.ImageField(null=True)
    date=models.CharField(max_length=100)
    description=models.TextField(max_length=500)
    def __str__(self):
        return str(self.title)

class projects(models.Model):
    name=models.CharField(max_length=100)
    description=models.TextField(max_length=500)
    image=models.ImageField(null=True)
    link=models.CharField(max_length=100)
    skillused=models.CharField(max_length=100)
    def __str__(self):
        return str(self.name)
