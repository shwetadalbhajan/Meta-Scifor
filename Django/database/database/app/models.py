from django.db import models

class Person(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    phone = models.IntegerField(null=True)
    joined_date = models.DateField(null=True)

    def __str__(self):
        return f"{self.firstname} {self.lastname}"

class College(models.Model):
    name = models.CharField(max_length=255)
    phone = models.IntegerField(max_length=10,null=True)
    college = models.CharField(max_length=255,null=True)
    address = models.TextField(null=True)
    age = models.IntegerField(max_length=2,null=True)
    qualification = models.CharField(max_length=255,null=True)

    def __str__(self):
        return f"{self.name}"
