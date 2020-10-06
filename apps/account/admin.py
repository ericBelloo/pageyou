from django.contrib import admin

from django.contrib import admin
from .models import Account, Calendar, Transactions


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    pass


@admin.register(Calendar)
class CalendarAdmin(admin.ModelAdmin):
    pass


@admin.register(Transactions)
class TransactionsAdmin(admin.ModelAdmin):
    pass
