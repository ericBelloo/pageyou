
from datetime import datetime, timedelta
from django.http import HttpResponseRedirect
from django.views.generic import FormView, ListView
from apps.account.forms import CreateAccountForm
from django.contrib.auth.models import Group
from django.contrib import messages
from apps.account.models import Calendar, Account
from django.urls import reverse

#utils
from utils.constants import Message


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
        account.group = group  # asigna el grupo
        account.status = 'DESEMBOLSADA'  # asigna el estado de la cuenta
        account.save()
        """ Set calendar """
        amount = form.cleaned_data['amount']
        payment_period = 12
        amount_week = round(float(amount) / payment_period, 2)  # 24: week in one year
        week_count = 1
        for item in range(1, payment_period + 1):
            payment_date = datetime.now() + timedelta(weeks=week_count)
            Calendar.objects.create(payment_number=week_count, amount=amount_week, payment_date=payment_date.strftime('%Y-%m-%d'), account=account)
            week_count += 1
        messages.success(request, Message.SUCCESS_SAVE)
        return HttpResponseRedirect(reverse('client:user_groups', args=[group.id]))


class CalendarView(ListView):
    template_name = 'account/account.html'

    def get_queryset(self):
        return Calendar.objects.filter(account_id=self.kwargs.get('pk'))

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(CalendarView, self).get_context_data(**kwargs)
        account = Account.objects.get(id=self.kwargs.get('pk'))
        context['account'] = account
        return context
