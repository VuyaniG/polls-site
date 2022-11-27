from django.urls import path
from . import views

app_name = 'user_auth'
urlpatterns = [
    path('', views.user_reg, name='user_reg'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('authenticate_user/', views.authenticate_user,
    name='authenticate_user'),
    path('user/', views.show_user, name = 'show_user'),]
