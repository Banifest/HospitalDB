from django.db import models


class Users(models.Model):
    id = models.IntegerField()
    type = models.IntegerField()
    nick = models.CharField(50)
    password = models.CharField(50)
    date_registration = models.DateField()
    fio = models.CharField(50)
    birthday = models.DateField()
