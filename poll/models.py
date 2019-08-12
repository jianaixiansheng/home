from django.db import models
import uuid
# Create your models here.



class Banner(models.Model):

    id = models.AutoField(primary_key=True)

    img = models.ImageField(upload_to = 'img/')


class infomation(models.Model):
    name = models.CharField(max_length=100)

    birthday = models.CharField(max_length=100)

    sex = models.CharField(max_length=100)

    addr = models.CharField(max_length=100)

    nation = models.CharField(max_length=100)

    IDcard = models.CharField(max_length=100)


