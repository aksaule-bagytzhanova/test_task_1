from django.db import models

# Create your models here.

class Area1Model(models.Model):
    name = models.CharField(max_length=200)
    discription = models.CharField(max_length=200)
    points = models.CharField(max_length=200)
    fill_type = models.CharField(max_length=200)
    color = models.CharField(max_length=200)
    class Meta:
        db_table='areas1'

class Area2Model(models.Model):
    name = models.CharField(max_length=200)
    discription = models.CharField(max_length=200)
    points = models.CharField(max_length=200)
    fill_type = models.CharField(max_length=200)
    color1 = models.CharField(max_length=200)
    color2 = models.CharField(max_length=200)
    angle = models.IntegerField()
    class Meta:
        db_table='areas2'