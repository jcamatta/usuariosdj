from django.urls import path, include
from . import views

app_name = 'users_app'

urlpatterns = [
    path('users/user_register', views.UserRegister.as_view(), name='user_register'),
]