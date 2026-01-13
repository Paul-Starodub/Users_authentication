from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from users.forms import CustomUserCreationForm, CustomUserLoginForm


def register(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user, backend="django.contrib.auth.backends.ModelBackend")
            return redirect("users:profile")
    else:
        form = CustomUserCreationForm()
    return render(request, "users/register.html", {"form": form})


def login(request):
    if request.method == "POST":
        form = CustomUserLoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user, backend="django.contrib.auth.backends.ModelBackend")
            return redirect("users:profile")
    else:
        form = CustomUserLoginForm()
    return render(request, "users/login.html", {"form": form})


@login_required
def profile(request):
    return render(request, "users/profile.html", {"user": request.user})
