
from django.urls import path
from apps.client import views
# model

app_name = 'client'

urlpatterns = [
    path('login/', views.LoginView.as_view(), name='login'),
    path('sign-up/', views.SignUpView.as_view(), name='sign_up'),
    path('new-group/', views.NewGroupView.as_view(), name='new_group'),
    # path('group/<str:group_name>', views.ClientListView.as_view(), name='groups'),

]
