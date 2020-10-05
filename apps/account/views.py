
from django.shortcuts import render
from django.views.generic import FormView
from apps.account.forms import CreateAccountForm


class CreateAccountView(FormView):
    form_class = CreateAccountForm
    template_name = 'account/new_account.html'


