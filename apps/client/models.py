
from django.contrib.auth.models import User
from django.db import models


class Client(models.Model):
    coordinator = models.BooleanField(default=False)
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
