from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request,'app/base.html')
def event(request):
    return render(request,'app/event.html')
def index(request):
    return render(request,'app/index.html')
