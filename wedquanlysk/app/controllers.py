from django.shortcuts import render

def event_manager_view(request):
    return render(request, 'event_manager.html')

def home_view(request):
    return render(request, 'base.html')
