from django.db import models

class Csv(models.Model):
    event = models.CharField(max_length=50, null= True)
    file = models.FileField(upload_to='input')
    activated = models.BooleanField(default=False)

    def __str__(self):
        return self.event

# Create your models here.
