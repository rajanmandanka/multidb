from django.db import models


# Create your models here.


class Demo1(models.Model):
    name = models.CharField(max_length=10)

    class Meta:
        app_label = 'app1'

class Demo2(models.Model):
    name = models.CharField(max_length=10)