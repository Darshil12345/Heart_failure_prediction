
# Create your views here.
from django.shortcuts import render, redirect

from django.contrib.auth.forms import AuthenticationForm

from django.contrib.auth import (
    login,
    logout,
    authenticate
)

from .forms import RegisterForm


def register_view(request):

    if request.method == "POST":

        form = RegisterForm(
            request.POST
        )

        if form.is_valid():

            form.save()

            return redirect(
                "login"
            )

    else:

        form = RegisterForm()

    return render(

        request,

        "register.html",

        {
            "form": form
        }

    )


def login_view(request):

    if request.method == "POST":

        username = request.POST[
            "username"
        ]

        password = request.POST[
            "password"
        ]

        user = authenticate(

            request,

            username=username,

            password=password

        )

        print("USERNAME =", username)
        print("USER =", user)

        if user is not None:

            login(
                request,
                user
            )

            return redirect(
                "home"
            )

    form = AuthenticationForm()

    return render(

        request,

        "login.html",

        {
            "form": form
        }

    )


def logout_view(request):

    logout(
        request
    )

    return redirect(
        "login"
    )