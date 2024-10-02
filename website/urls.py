from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    #path('login/', views.login_user, name='login'), Use if want to create seperate login page 
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.logout_user, name='register'),
]