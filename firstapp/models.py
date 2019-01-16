from django.contrib.auth.models import User
from django.db import models


class CalcHistory(models.Model):
    date = models.DateTimeField()
    first = models.IntegerField()
    second = models.IntegerField()
    result = models.IntegerField()
    author = models.ForeignKey(to=User, on_delete=models.SET_NULL, null=True)
