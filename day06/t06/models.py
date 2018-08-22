from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class MyUser(AbstractUser):
    sex_choice = (
        (1,'男'),
        (2,'女'),
        (3,'男女')
    )
    age = models.IntegerField(
        verbose_name='年龄'
    )
    phone = models.CharField(
        max_length=13,
        verbose_name='联系方式'
    )
    sex = models.IntegerField(
        choices=sex_choice,
        verbose_name='性别'
    )
    icon = models.ImageField(
        upload_to='icons',
        null = True,
        verbose_name='图片'
    )
    iconurl = models.CharField(
        max_length=255,
        null=True,
        verbose_name='图片路径'
    )