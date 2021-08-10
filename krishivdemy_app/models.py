from django.db import models


# Create your models here.
class Year(models.Model):
    year = models.IntegerField()


class Month(models.Model):
    month = models.CharField(max_length=11)


class Date(models.Model):
    date = models.IntegerField()
