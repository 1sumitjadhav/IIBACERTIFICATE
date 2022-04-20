from wsgiref.validate import validator
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
import secrets
from django.db.models.signals import post_save
import random

class Coupon_gener(models.Model): 
       
    # Model field for our unique code
    # coupon = models.BooleanField(default=False)
    code = models.CharField(max_length=8, blank=True, null=True, unique=True)

    def __str__(self):
        return "%s" % (self.code)
class coupon(models.Model):
    # coupon =  models.BooleanField(default=False)
    code = models.CharField(max_length=20)
    def __str__(self):
        return self.code
    

# Create your models here.
