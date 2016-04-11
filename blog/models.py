from __future__ import unicode_literals
from django.db import models
# from blog.models import CsvDbModel

from data_importer.importers import XLSImporter
import sys
from datetime import datetime
#pip install django-adaptors

# Create your models here.



class Review(models.Model):
   title = models.CharField(max_length=100)
   review = models.CharField(max_length=500)
   name = models.CharField(max_length=255)
   created_date = models.DateTimeField('date created')


class Great_Britian(models.Model):
   unit_name=models.CharField(max_length=100)
   class_name=models.CharField(max_length=100)
   description=models.CharField(max_length=100000)
   men_count=models.CharField(max_length=100)
   guns=models.CharField(max_length=100)
   firepower=models.CharField(max_length=100)
   range=models.CharField(max_length=100)
   accuracy=models.CharField(max_length=100)
   reloading_skill=models.CharField(max_length=100)
   ammo=models.CharField(max_length=100)
   strength=models.CharField(max_length=100)
   speed=models.CharField(max_length=100)
   value=models.CharField(max_length=100)
   defense=models.CharField(max_length=100)


# class GBcsvModel(CsvDbModel):
   # unit_name=models.CharField()
   # class_name=models.CharField()
   # description=models.CharField()
   # men_count=models.IntegerField(default=0)
   # guns=models.IntegerField(default=0)
   # firepower=models.IntegerField(default=0)
   # range=models.IntegerField(default=0)
   # accuracy=models.IntegerField(default=0)
   # reloading_skill=models.IntegerField(default=0)
   # ammo=models.IntegerField(default=0)
   # strength=models.IntegerField(default=0)
   # speed=models.IntegerField(default=0)
   # value=models.IntegerField(default=0)
   # defense=models.IntegerField(default=0)

   # class Meta:
   #      dbModel = Great_Britian
   #      delimiter=str(',')