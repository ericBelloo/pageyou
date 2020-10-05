
from django.urls import path
from apps.client import views
# model

app_name = 'client'

urlpatterns = [
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.logout, name='logout'),
    path('sign-up/', views.SignUpView.as_view(), name='sign_up'),
    path('new-group/', views.NewGroupView.as_view(), name='new_group'),
    path('search-group/', views.ClientSearchGroupListView.as_view(), name='search_groups'),
    path('user-group/<int:pk>/', views.ClientGroupList.as_view(), name='user_groups'),
]
