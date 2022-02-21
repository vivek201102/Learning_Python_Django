from django.urls import path, include
from . import views

urlpatterns = [
    #setup profile
    path('setup', views.setup, name="setup"),
]