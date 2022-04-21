from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    is_student = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

class Student(models.Model):
    user = models. OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    email_id= models.CharField(max_length=20)
    phone_no= models.CharField(max_length=10)


class Teacher(models.Model):
    user = models. OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    email_id= models.CharField(max_length=20)
    phone_no= models.CharField(max_length=10)

