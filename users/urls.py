from django.urls import path
from users.views import register, login, profile

app_name = "users"

urlpatterns = [
    path("register/", register, name="register"),
    path("login/", login, name="login"),
    path("profile/", profile, name="profile"),
]
