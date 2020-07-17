from django.shortcuts import render
from django.views.generic import TemplateView, View
# Create your views here.


class HomeView(TemplateView):
    template_name = 'home.html'


class InitialInvestment(TemplateView):
    template_name = 'capital_prestado.html'


class TMARView(TemplateView):
    template_name =  'tmar.html'


class FNEView(TemplateView):
    template_name = 'fne.html'