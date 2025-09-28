from django.urls import path
from .views import register_view, profile_view, UserLoginView, profile_edit_view
from django.contrib.auth.views import LogoutView

app_name = "users"

urlpatterns = [
    path("register/", register_view, name="register"),
    path("profile/", profile_view, name="profile"),
    path("login/", UserLoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(next_page="catalog:home"), name="logout"),
    path("profile/edit/", profile_edit_view, name="profile_edit")
]
