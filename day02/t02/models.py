from django.db import models

# Create your models here.
class People(models.Model):
    name = models.CharField(
        max_length=30,
        verbose_name='名字'
    )
    age = models.IntegerField()
    sexy = models.CharField(
        max_length=10,
        verbose_name='性别'
    )
    birthday = models.DateField(
        verbose_name="出生日期"
    )
    is_married = models.BooleanField(
        default=False,
        verbose_name="是否已婚"
    )
    class Meta():
        verbose_name="个人信息",
        db_table = "person_imformation"