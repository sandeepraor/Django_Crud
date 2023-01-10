from django.urls import include,path
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    path('login/', views.loginUser, name="login"),
    path('register/', views.register, name="register"),
    path('profile/', views.profile, name="profile"),
    path('logout/', views.logoutUser),
    path('add_user_details',views.add_user_detail),
    path('edit_user_details',views.edit_user_details),
    path('update_user_details',views.update_user_details)
]