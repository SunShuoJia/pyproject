from django.db import models

# Create your models here.
class Home(models.Model):
    name = models.CharField(
        max_length=30,
        verbose_name='家庭'
    )

class Person(models.Model):
    name = models.CharField(
        verbose_name='名字',
        max_length=30
    )
    age = models.IntegerField(
        verbose_name='年龄'
    )
    home = models.ForeignKey(
        Home,
        null=True
    )
    class Meta:
        verbose_name='人'

