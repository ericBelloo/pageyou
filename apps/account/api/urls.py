
from django.urls import path
from apps.account.api import views

app_name = 'api_account'

urlpatterns = [
    path('transaction/', views.SaveTransaction.as_view(), name='transaction'),
]
