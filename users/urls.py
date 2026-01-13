from django.urls import path
from users.views import (
    register,
    login_view,
    profile,
    account_details,
    edit_account_details,
    update_account_details,
    logout_view,
)

app_name = "users"

urlpatterns = [
    path("register/", register, name="register"),
    path("login/", login_view, name="login"),
    path("profile/", profile, name="profile"),
    path("account-details/", account_details, name="account_details"),
    path("edit-account-details/", edit_account_details, name="edit_account_details"),
    path("update-account-details/", update_account_details, name="update_account_details"),
    path("logout/", logout_view, name="logout"),
]
