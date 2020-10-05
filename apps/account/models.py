from django.db import models
from django.contrib.auth.models import Group
from utils.mixins import BaseDateModel


class Account(BaseDateModel):
    status = models.CharField(max_length=100, null=False, blank=False)  # estatus
    amount = models.DecimalField(max_digits=10, decimal_places=2)  # monto por pagar
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0)  # saldo

    # Foreign Key
    group = models.ForeignKey(Group, null=True, on_delete=models.SET_NULL)


class Calendar(models.Model):

    payment_number = models.IntegerField(default=0)  # numero de pago
    amount = models.DecimalField(max_digits=10, decimal_places=2)  # monto
    payment_date = models.DateField(null=False, blank=False)  # fehca de pago
    status = models.CharField(max_length=100, null=False, blank=False)  # estatus

    # Foreign Key
    account = models.ForeignKey(Account, null=True, blank=False, on_delete=models.SET_NULL)


class Transactions(models.Model):

    date = models.DateField(null=False, blank=False)
    amount = models.DecimalField(max_digits=10, decimal_places=2)  # monto

    # Foreign Key
    account = models.ForeignKey(Account, null=True, blank=False, on_delete=models.SET_NULL)
