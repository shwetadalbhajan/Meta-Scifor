from django.db import models
from rest_framework import serializers

class MyModel(models.Model):
    author = models.CharField(max_length=255)
    title = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.author}'