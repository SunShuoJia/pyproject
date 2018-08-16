from django.db import models

# Create your models here.
class language(models.Model):
    name = models.CharField(
        max_length=20,
        verbose_name="方言"
    )
    describe = models.TextField(
        null=True,
        max_length=1000,
        verbose_name="描述"
    )