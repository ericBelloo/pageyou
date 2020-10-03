
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.views import FormView
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate
from django.contrib import messages
from utils.constants import Message
# forms
from apps.client.forms import ClientLoginForm, ClientSignUpForm


class LoginView(SuccessMessageMixin, FormView):
    template_name = 'client/login.html'
    form_class = ClientLoginForm
    success_url = 'blog-home'
    success_message = ''

    def form_valid(self, form):
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            """ User authenticate """
            return HttpResponseRedirect(self.get_success_url())
        else:
            messages.error(self.request, Message.ERROR_LOGIN)
            return self.render_to_response(self.get_context_data(form=form))


class SignUpView(SuccessMessageMixin, FormView):
    template_name = 'client/sign_up.html'
    form_class = ClientSignUpForm
    success_url = 'client/sign_up.html'
    success_message = ''

    def form_valid(self, form):
        return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self, form):
        messages.error(self.request, form.errors)
        return self.render_to_response(self.get_context_data(form=form))