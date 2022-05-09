from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('search', views.search, name='search'),
    path('create', views.create, name='create'),
    path('login', views.loginpage, name='login'),
    path('loginuser', views.loginUser, name='login-user'),
]