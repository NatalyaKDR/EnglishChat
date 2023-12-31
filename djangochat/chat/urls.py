from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns=[
    path('', views.frontpage, name='frontpage'),
    path('signup/', views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='chat/login.html'), name='login'), #тут без view , взяли стандартный класс
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),#тут без view , взяли стандартный класс
]