from __future__ import unicode_literals
from django.db import models
from datetime import datetime


# Create your models here.



class Review(models.Model):
   title = models.CharField(max_length=100)
   review = models.CharField(max_length=500)
   name = models.CharField(max_length=255)
   created_date = models.DateTimeField('date created')