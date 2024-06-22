from django.urls import path
from users.apps import UsersConfig
from django.contrib.auth.views import LoginView
from users.views import RegisterView,ProfileView,generate_new_password,email_verification,UserListView,UserDetailView,UserDeleteView,logout_view

app_name = UsersConfig.name

urlpatterns = [
    path('register/',RegisterView.as_view(),name='register'),
    path('login/',LoginView.as_view(template_name='users/login.html'),name='login'),
    path('logout/',logout_view,name='logout'),
    path('profile/edit_user/<int:pk>/',ProfileView.as_view(),name='profile'),
    path('profile/newpassword', generate_new_password, name='generate_new_password'),
    path('confirm/<str:token>', email_verification, name='confirm'),
    path('user_list/', UserListView.as_view(), name='user_list'),
    path('profile/view_user/<int:pk>/', UserDetailView.as_view(), name='view_user'),
    path('profile/delete_user/<int:pk>/', UserDeleteView.as_view(), name='delete_user'),

]