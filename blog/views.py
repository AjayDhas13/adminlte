from django.contrib import auth
from django.contrib.auth import REDIRECT_FIELD_NAME
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render


def login_view(request, redirect_field_name=REDIRECT_FIELD_NAME):
    redirect_to = request.POST.get("next") or request.GET.get(redirect_field_name, "")

    if request.method == "POST":
        if not redirect_to or "//" in redirect_to or " " in redirect_to:
            redirect_to = "/home/"

        username = request.POST.get("username", "")
        password = request.POST.get("password", "")
        user = auth.authenticate(request, username=username, password=password)

        if user is not None and user.is_active:
            auth.login(request, user)
            return redirect(redirect_to)
        return HttpResponseRedirect("/register/")

    return render(request, "login.html", {"form": None})


def register(request):
    return render(request, "register.html", {"register": "Register Page"})


def home(request):
    return render(request, "blog/home.html", {"home": "It's a home content"})
