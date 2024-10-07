from django.db import models

# Create your models here.
class Book(models.Model):
    author = models.CharField(max_length=30)
    name_father_Author = models.CharField(max_length=4)
    title = models.TextField()
    publisher = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    year = models.IntegerField()
    pages = models.IntegerField()

class Journal(models.Model):
    author = models.CharField(max_length=30)
    name_father_Author = models.CharField(max_length=4)
    title = models.CharField(max_length=200)
    publisher = models.CharField(max_length=50)
    number_tom = models.IntegerField()
    year = models.IntegerField()
    page_start = models.IntegerField()
    page_end = models.IntegerField()

class Conf(models.Model):
    author = models.CharField(max_length=30)
    name_father_Author = models.CharField(max_length=4)
    title = models.CharField(max_length=200)
    publisher = models.CharField(max_length=150)
    place = models.CharField(max_length=20)
    date = models.DateField()
    year = models.IntegerField()
    city = models.CharField(max_length=20)
    page_start = models.IntegerField()
    page_end = models.IntegerField()