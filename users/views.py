from django.contrib.auth import login
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
from .forms import UserUpdateForm

from .forms import UserRegisterForm, UserLoginForm


def register_view(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)

            # Отправка письма
            send_mail(
                "Добро пожаловать!",
                "Спасибо за регистрацию в нашем магазине 🎉",
                "shop@example.com",
                [user.email],
                fail_silently=True,
            )

            return redirect("catalog:home")
    else:
        form = UserRegisterForm()
    return render(request, "users/register.html", {"form": form})


class UserLoginView(LoginView):
    template_name = "users/login.html"
    authentication_form = UserLoginForm
    redirect_authenticated_user = True


class UserLogoutView(LogoutView):
    next_page = reverse_lazy("catalog:home")

@login_required
def profile_view(request):
    if request.method == "POST":
        form = UserUpdateForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect("users:profile")
    else:
        form = UserUpdateForm(instance=request.user)
    return render(request, "users/profile.html", {"form": form})

@login_required
def profile_edit_view(request):
    if request.method == "POST":
        form = UserUpdateForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect("users:profile")
    else:
        form = UserUpdateForm(instance=request.user)

    return render(request, "users/profile_edit.html", {"form": form})