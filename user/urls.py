from django.urls import include,path
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    path('login/', views.loginUser, name="login"),
    path('register/', views.register, name="register"),
    path('profile/', views.profile, name="profile"),
    path('logout/', views.logoutUser),
]