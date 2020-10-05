from django.contrib.auth.mixins import LoginRequiredMixin

from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate
from django.contrib import messages
from django.views.generic import FormView
from django.views.generic.list import ListView
from django.contrib.auth.models import Group

from utils.constants import Message
# forms
from apps.client.forms import ClientLoginForm, NewGroupView, UserSignUpForm
from apps.client.models import Client


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
    form_class = UserSignUpForm
    success_url = 'client/sign_up.html'
    success_message = ''

    def form_valid(self, form):
        user = form.save()
        if form.is_valid():
            """ Save new client """
            client = Client.objects.create(user=user)
            client.save()
        return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self, form):
        """ Create client error """
        messages.error(self.request, form.errors)
        return self.render_to_response(self.get_context_data(form=form))


class NewGroupView(FormView):
    """ Create new group """
    # login_url = '/client/login/'
    # redirect_field_name = 'redirect_to'
    template_name = 'client/group.html'
    form_class = NewGroupView

    def form_valid(self, form):
        """ Assignment of a coordinator to the group """
        group = form.save()  # create new group
        client_id = self.request.POST.get('client_id')
        client = Client.objects.get(id=client_id)  # get client
        client.coordinator = True   # set coordinator
        client.save()
        group.user_set.add(client.user)  # add client to new group

    def form_invalid(self, form):
        """ Create client error """
        messages.error(self.request, form.errors)
        return self.render_to_response(self.get_context_data(form=form))


class ClientSearchGroupListView(ListView):
    """ user group list """
    template_name = ''
    paginate_by = 5

    def get_queryset(self):
        name = self.request.GET.get('name')
        if name != '':
            return Group.objects.filter(name__contains=name)
        else:
            return Group.objects.all()


class ClientGroupList(ListView):
    template_name = ''

    def get_queryset(self):
        """ Show all group clients """
        group = Group.objects.get(name=self.request.user.group)
        return group.user_set.all()
