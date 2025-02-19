from django.urls import path
from .controllers import event_manager_view, home_view

urlpatterns = [
    path('', home_view, name='home'),
    path('event_manager/', event_manager_view, name='event_manager'),
]
