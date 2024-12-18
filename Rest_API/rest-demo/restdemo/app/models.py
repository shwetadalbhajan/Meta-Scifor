from django.db import models

class Data(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    job_title = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name}"