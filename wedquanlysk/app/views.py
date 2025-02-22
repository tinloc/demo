from django.shortcuts import render, redirect
from .models import Register
from django.http import HttpResponse
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request,'app/base.html')
def event(request):
    return render(request,'app/event.html')

def index(request):
    if request.method == "POST":
        hoten = request.POST.get("hoten", "").strip()
        email = request.POST.get("email", "").strip()
        sodienthoai = request.POST.get("sodienthoai", "").strip()

        if not hoten or not email or not sodienthoai:
            messages.error(request, "Vui lòng điền đầy đủ thông tin!")
        elif Register.objects.filter(email=email).exists():
            messages.error(request, "Email này đã được đăng ký!")
        else:
            Register.objects.create(hoten=hoten, email=email, sodienthoai=sodienthoai)
            messages.success(request, "Đăng ký thành công!")

        return redirect("home")  # Điều hướng về trang chủ hoặc chính trang hiện tại

    participants = Register.objects.all()
    return render(request, "app/index.html", {"participants": participants})


def register(request):
    return render(request,'app/register.html')
def sukien(request):
    return render(request,'app/sukien.html')
def event_manager(request):
    return render(request,'app/event_manager.html')
def review(request):
    return render(request,'app/review.html')
def survey(request):
    return render(request,'app/survey.html')
