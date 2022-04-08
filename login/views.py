from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages

def index(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        auth = authenticate(request, username=username, password=password)
        if auth is not None:
            login(request, auth)
            return redirect('dashboard:index')
        else:
            messages.warning(request, "Login Failed ! Check Your Credentials.")
            return redirect("login:index")
    return render(request, "login/index.html")
