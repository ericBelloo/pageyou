from django.contrib.auth.mixins import LoginRequiredMixin

from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import Q
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import FormView
from django.views.generic.list import ListView
from django.contrib.auth.models import Group, User
from utils.constants import Message
# forms
from apps.client.forms import ClientLoginForm, NewGroupView, UserSignUpForm
from apps.client.models import Client


class LoginView(SuccessMessageMixin, FormView):
    template_name = 'client/login.html'
    form_class = ClientLoginForm
    success_url = '/client/new-group/'

    def form_valid(self, form):
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            """ User authenticate """
            login(self.request, user)
            user = User.objects.get(username=username)
            group = user.groups.count()
            if group > 0:
                return HttpResponseRedirect(reverse('client:search_groups'))
            else:
                return HttpResponseRedirect(self.get_success_url())
        else:
            messages.error(self.request, Message.ERROR_LOGIN)
            return self.render_to_response(self.get_context_data(form=form))


def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/client/login/')


class SignUpView(SuccessMessageMixin, FormView):
    template_name = 'client/sign_up.html'
    form_class = UserSignUpForm
    success_message = 'El usuario se creo correctamente'

    def form_valid(self, form):
        user = form.save()
        if form.is_valid():
            """ Save new client """
            client = Client.objects.create(user=user)
            client.save()
            messages.success(self.request, Message.SUCCESS_LOGIN)
        return HttpResponseRedirect('/client/login/')

    def form_invalid(self, form):
        """ Create client error """
        messages.error(self.request, form.errors)
        return self.render_to_response(self.get_context_data(form=form))


class NewGroupView(FormView):
    """ Create new group """
    # login_url = '/client/login/'
    # redirect_field_name = 'redirect_to'
    template_name = 'client/new_group.html'
    form_class = NewGroupView
    success_url = '/client/new-group/'

    def form_valid(self, form):
        """ Assignment of a coordinator to the group """
        group = form.save()  # create new group
        user = User.objects.get(username=self.request.user)  # get user
        client = Client.objects.get(user=user)
        client.coordinator = True   # set coordinator
        client.save()
        group.user_set.add(client.user)  # add client to new group
        messages.success(self.request, Message.SUCCESS_SAVE)
        return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self, form):
        """ Create client error """
        messages.error(self.request, form.errors)
        return self.render_to_response(self.get_context_data(form=form))


class ClientSearchGroupListView(ListView):
    """ user group list """
    template_name = 'client/search_group.html'
    paginate_by = 5
    model = Group

    def get_queryset(self):
        filter_partial = Q()
        name = self.request.GET.get('name' or None)
        if name and name != '':
            partial_name = Q(name__icontains=name)
            filter_partial &= partial_name
        queryset = self.model.objects.filter(filter_partial)
        return queryset


class ClientGroupList(SuccessMessageMixin, ListView):
    """ Shows group users  """
    success_message = 'El usuario se agrego correctamente'
    template_name = 'client/user_group.html'
    model = Group

    def get_queryset(self):
        """ Show all group clients """
        group = self.model.objects.get(id=self.kwargs.get('pk'))
        return group.user_set.all()

    def get_context_data(self, **kwargs):
        context = super(ClientGroupList, self).get_context_data(**kwargs)
        group_count = self.model.objects.get(id=self.kwargs.get('pk')).user_set.all()
        user = User.objects.get(username=self.request.user)  # get user
        group = self.model.objects.get(id=self.kwargs.get('pk'))
        if user in group_count:
            context['member'] = True
        else:
            context['member'] = False
        if group_count.count() >= 4 and user.has_perm('client.coordinator'):
            account = True
        else:
            account = False
        context['group'] = group
        context['account'] = account
        return context

    def post(self, *args, **kwargs):
        group = self.model.objects.get(id=self.kwargs.get('pk'))
        user = User.objects.get(username=self.request.user)  # get user
        group.user_set.add(user)  # add client to new group
        return HttpResponseRedirect(self.request.META.get('HTTP_REFERER'))