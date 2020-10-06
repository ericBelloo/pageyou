
from datetime import datetime, date

from django.http import HttpResponseRedirect
from django.views.generic import FormView
from apps.account.forms import CreateAccountForm
from django.contrib.auth.models import Group
from django.contrib import messages
from apps.account.models import Calendar


class CreateAccountView(FormView):
    form_class = CreateAccountForm
    template_name = 'account/new_account.html'

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            account = form.save()
        else:
            messages.error(request, form.errors)
            return HttpResponseRedirect(self.request.META.get('HTTP_REFERER'))
        group = Group.objects.get(id=self.kwargs.get('pk'))
        account.group = group
        account.save()
        """ Set calendar """
        amount = form.cleaned_data['amount']
        payment_period = 24
        amount_week = round(float(amount) / 24, 2)  # 24: week in one year
        for item in range(1, payment_period + 1):
            count = 1
            payment_date = date.today() + datetime.timedelta(weeks=count)
            Calendar.objects.create(payment_number=count, amount=amount_week, payment_date=payment_date, account=account)
        return HttpResponseRedirect(self.request.META.get('HTTP_REFERER'))

