from django.contrib import admin
from django.urls import path
from.import views

urlpatterns = [
    path('', views.home),
    path('event/', views.event, name='event'),
    path('index/', views.index, name='index'),
]