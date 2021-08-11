from django.db import models


# Create your models here.
class Year(models.Model):
    year = models.IntegerField()


class Month(models.Model):
    year = models.ForeignKey(Year, on_delete=models.CASCADE, null=True)
    month = models.CharField(max_length=11)


class Date(models.Model):
    month = models.ForeignKey(Month, on_delete=models.CASCADE, null=True)
    date = models.IntegerField()


class Page(models.Model):
    date = models.ForeignKey(Date, on_delete=models.CASCADE)
class Text(models.Model):
    page=models.ForeignKey(Page,on_delete=models.CASCADE,null=True)
    text=models.TextField()
