from django.db import models

# Create your models here.
class movie(models.Model):
    name = models.CharField(
        max_length=30
    )
    heat = models.IntegerField(
        max_length=10
    )