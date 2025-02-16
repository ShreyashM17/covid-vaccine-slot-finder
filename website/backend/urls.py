from django.urls import path, include
from .views import homepage, login, signup, verified, password, locator, slot, resetpass, logout

urlpatterns = [
    path("", homepage, name="home"),
    path("login/", login, name="login"),
    path("signup/", signup, name="signup"),
    path("verify/<str:uid>", verified, name="verify"),
    path("verify/password/<str:uid>", password, name="password"),
    path("slotfinder/<str:email_id>", locator, name="locate"),
    path("slotfinder/<str:email_id>/slots", slot, name="slot"),
    path("login/resetpass/", resetpass, name="reset"),
    path("logout/<str:uid>", logout, name="logout"),
]