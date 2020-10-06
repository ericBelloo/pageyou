
from django.urls import path
from apps.account import views
# model

app_name = 'account'

urlpatterns = [
    path('new-account/<int:pk>/', views.CreateAccountView.as_view(), name='new_account'),
    path('calendar/<int:pk>/', views.CalendarView.as_view(), name='calendar')
]
