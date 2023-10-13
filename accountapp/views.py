from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render

from accountapp.forms import LoginForm, UserRegistrationForm


def register(request):
    if request.method == "POST":
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data["password"])
            new_user.save()

            return render(request, "accountapp/register_done.html", {"new_user": new_user})
    else:
        user_form = UserRegistrationForm()

    return render(request, "accountapp/register.html", {"user_form": user_form})
