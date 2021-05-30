#  website/urls.py

from django.shortcuts import render
from . import views
from django.urls import path

app_name = "website"

urlpatterns = [
    path('', views.home_page_view, name='home'),
    path('sobre', views.sobre_page_view, name='sobre'),
    path('contatos', views.contatos_page_view, name='contatos'),
]