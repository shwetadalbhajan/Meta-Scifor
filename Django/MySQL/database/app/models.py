from django.db import models

class Data(models.Model):
    Name = models.CharField(max_length=200)
    Age = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.Name