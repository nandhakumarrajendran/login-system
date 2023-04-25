from django.urls import path
from Login_App import views

urlpatterns = [
    path('', views.Home, name='Home'),
    path('home', views.Home, name='Home'),
    path('login', views.Loginpage, name='Login'),
    path('signup', views.Signuppage, name='Signup'),
    path('profile', views.Profile, name='Profile'),
    path('logout', views.logoutpage, name='Logout'),
]
