
from django.urls import path
from apps.home.views import *

app_name = 'home'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('inversion-inicial/', InitialInvestment.as_view(), name='inversion_inicial'),
    path('tmar/', TMARView.as_view(), name='tmar'),
    path('fne/', FNEView.as_view(), name='fne'),
]
