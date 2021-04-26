
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.honePage, name='home'),
    path('search', views.new_search, name='search'),
]
