from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .forms import CustomUserCreationForm, CustomAuthenticationForm

def signup_view(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("questionnaire:fill")
    else:
        form = CustomUserCreationForm()
    return render(request, "users/signup.html", {"form": form})

def login_view(request):
    if request.method == "POST":
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("home:index")
    else:
        form = CustomAuthenticationForm()
    return render(request, "users/login.html", {"form": form})

def logout_view(request):
    logout(request)
    return redirect("home:index")

def guest_view(request):
    # Guest users are not stored in DB, just session-based
    request.session["subscription"] = "guest"
    return redirect("questionnaire:fill")
