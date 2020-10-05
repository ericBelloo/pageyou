
from django.contrib.auth.models import User
from django.db import models


class Client(models.Model):
    coordinator = models.BooleanField(default=False)
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.user.username

    class Meta:
        permissions = (("coordinator", "Set coordinator group"),)
