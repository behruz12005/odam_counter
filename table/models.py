from django.db import models

class Element(models.Model):
    name = models.CharField(max_length=100)
    data = models.CharField(max_length=100)
    voqt = models.CharField(max_length=100)
    values = models.CharField(max_length=100)