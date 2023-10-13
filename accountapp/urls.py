from django.contrib.auth import views as auth_views
from django.urls import path

from accountapp import views as accountapp_views
from recipeapp import views as recipeapp_views

urlpatterns = [
    path("login/", auth_views.LoginView.as_view(), name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("register/", accountapp_views.register, name="register"),
    path("", recipeapp_views.random_recipes, name="random_recipes"),
]
