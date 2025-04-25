from django.urls import path
from . import views
from .googleGraph import googleGraph

app_name = "home_module"

urlpatterns = [
    path("", views.home, name='home page'),
    path("google-graph", googleGraph, name='Google graph')
]
