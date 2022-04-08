from wsgiref.validate import validator
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
import secrets
from django.db.models.signals import post_save
import random

class Coupon(models.Model): 
       
    # Model field for our unique code
    code = models.CharField(max_length=8, blank=True, null=True, unique=True)

    def __str__(self):
        return "%s" % (self.code)
