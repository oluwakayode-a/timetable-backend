from django.urls import path
from .views import CreateUser, LoginView, CurrentUser

urlpatterns = [
    path("sign_up/", CreateUser.as_view()),
    path("login/", LoginView.as_view()),
    path("me/", CurrentUser.as_view())
]