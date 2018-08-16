from django.db import models

# Create your models here.
class Team(models.Model):
    name = models.CharField(
        max_length=30,
        verbose_name="队名"
    )
    def __str__(self):
        return self.name

class Player(models.Model):
    name = models.CharField(
        max_length=30,
        verbose_name="名字"
    )
    age = models.IntegerField(
        verbose_name="年龄"
    )
    is_live = models.BooleanField(
        verbose_name="是否在役"
    )
    team = models.ForeignKey(
        Team,
        null=True,
        verbose_name="归属球队"
    )
    def __str__(self):
        return self.name

class IdCard(models.Model):
    num = models.CharField(
        max_length=19,
        verbose_name="身份证号"
    )
    org = models.CharField(
        max_length=30,
        verbose_name="签发单位"
    )

class Person(models.Model):
    name = models.CharField(
        max_length=30,
        verbose_name="姓名"
    )
    idcard = models.OneToOneField(
        IdCard,
        on_delete=models.PROTECT
    )

class Author(models.Model):
    name = models.CharField(
        max_length=30,
        verbose_name="名字"
    )
    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(
        max_length=30,
        verbose_name="书名"
    )
    author = models.ManyToManyField(
        Author,
        verbose_name="作者"
    )
    def __str__(self):
        return self.title

class Humen(models.Model):
    name = models.CharField(
        max_length=30,
        verbose_name="姓名"
    )
    age = models.IntegerField(
        verbose_name="年龄"
    )
    height = models.FloatField(
        verbose_name="身高"
    )
    class Meta:
        #声明此类是抽象类
        abstract = True

class Boy(Humen):
    salary = models.CharField(
        max_length=30,
        verbose_name="工资"
    )

class Girl(Humen):
    face_score = models.IntegerField(
        verbose_name="颜值"
    )

class HeHe(models.Model):
    suibian = models.IntegerField(
        null=True
    )
    class Meta:
        abstract = True

class DuoJiCheng(Humen,HeHe):
    # 多继承
    salsry = models.CharField(
        max_length=30
    )