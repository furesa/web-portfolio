from django.db import models


class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    technology = models.CharField(max_length=20)
    image = models.FilePathField(path="/pdf")
    logo = models.FilePathField(path="/img")


class Cheatsheet(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    links = models.CharField(max_length=20)
    image = models.FilePathField(path="/pdf")
    logo = models.FilePathField(path="/img")
