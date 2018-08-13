from django.db import models

# Create your models here.
class Engineer(models.Model):
    name = models.CharField(
        max_length=30,
        verbose_name="名字"
    )
    age = models.IntegerField(
        default=18
    )
    def __str__(self):
        return self.name

#车辆模型
class Cars(models.Model):
    name = models.CharField(
        max_length=30
    )
    color = models.CharField(
        max_length=30
    )
    def __str__(self):
        return self.name

#司机模型
class Drivers(models.Model):
    name = models.CharField(
        max_length=30
    )
    #指定外键
    car = models.ForeignKey(
        Cars,
        verbose_name="车"
    )
    def __str__(self):
        return self.name

