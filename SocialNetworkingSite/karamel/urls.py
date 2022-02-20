from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    #index page path
   path('', views.index, name="index"),
   #login page redirection
   path('login', views.login, name="login"),
   #Signup page redirection
   path('signup', views.signup, name="signup"),
   #About page redirection
   path("about", views.about, name="about"),
   #Register User
   path("register", views.register, name="register"),
   #Authenticate User
   path("auth", views.auth, name="auth"),

]