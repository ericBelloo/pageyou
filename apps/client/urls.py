
from django.urls import path
from apps.client import views
# model

app_name = 'client'

urlpatterns = [
    path('login/', views.LoginView.as_view(), name='login'),
    path('sign_up/', views.SignUpView.as_view(), name='sign_up'),
]
