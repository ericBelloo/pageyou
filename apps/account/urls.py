
from django.urls import path
from apps.account import views
# model

app_name = 'account'

urlpatterns = [
    path('new-account/', views.CreateAccountView.as_view(), name='new_account'),
]