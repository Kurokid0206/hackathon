from django.contrib.auth.models import User
from django.db import models


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    reference_id = models.CharField(max_length=100, blank=True, null=True)
    point = models.IntegerField(default=0)
    
    def __str__(self):
        return self.user.username


class GarbageType(models.TextChoices):
    RECYCLABLE = 'RECYCLABLE'
    ORGANIC = 'ORGANIC'
    HAZARDOUS = 'HAZARDOUS'
    SOLID = 'SOLID'
    LIQUID = 'LIQUID'


class Garbage(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100, choices=GarbageType.choices)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100)
    