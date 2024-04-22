from django.shortcuts import render, redirect
from django.urls import reverse
from .form import SignUpForm, LogInForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

def sign_or_log(request):
    return render(request, "sign_or_log.html")

def signup(request):
    sign=SignUpForm()
    if request.method == 'POST':
        sign=SignUpForm(request.POST,request.FILES)
        if sign.is_valid(): 
            sign.save()
            return redirect(reverse('course_app:home'))
    return render(request, "signup.html", {'sign':sign})

def login_page(request):
    errors=""
    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect(reverse('course_app:home'))
        else:
            errors+="Login yoki Parol noto'g'ri iltimos qayta urunib ko'ring!"
            return render(request, "login.html", {'errors':errors})
    return render(request, "login.html", {'errors':errors})

def logoutdef(request):
    logout(request)
    return redirect(reverse("course_app:home"))