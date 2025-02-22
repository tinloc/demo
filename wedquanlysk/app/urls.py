from django.contrib import admin
from django.urls import path
from.import views

urlpatterns = [
    path('', views.home,name='home'),
    path('event/', views.event, name='event'),
    path('event/sukien', views.sukien, name='sukien'),
    path('index/', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('event/event_manager/', views.event_manager, name='event_manager'),
    path('event/event_manager/review/', views.review, name='review'),
    path('event/event_manager/review/survey/', views.survey, name='survey'),
]