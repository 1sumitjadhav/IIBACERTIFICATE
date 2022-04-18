from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User
from input.models import Csv


class Student(models.Model):
    user = models.CharField(max_length=50, null= True, )
    email = models.EmailField(unique=True, null=True)
    first_name = models.CharField(max_length=50, null=True)
    last_name = models.CharField(max_length=50, null=True)
    course = models.CharField(max_length=50, null=True)
    activated = models.BooleanField(default=False)
    
    

    def __str__(self):
        return (self.user)



# Create your models here.
