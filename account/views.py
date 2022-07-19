from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.urls import reverse
from .forms import *
from .models import User


def register(request):
    if request.method == "GET":
        return render(request, "register.html", {"form": CustomUserCreationForm})
    elif request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(reverse("home"))
        else:
            name_errors = form.errors
            name_errors = list(name_errors.keys())
            info_name_errors = {
                "email": "Почта уже зарегистрирована.",
                "password2": "Пароли некорректны или  не совпадают.",
                "username": "Такой user  уже есть.",
            }
            info_errors = []
            for i in name_errors:
                info_errors.append(info_name_errors[i])
            return render(
                request,
                "register.html",
                {"form": CustomUserCreationForm, "info_errors": info_errors},
            )


def NewEmailProfile(request):
    if request.method == "GET":
        return render(
            request,
            "profile_newdata.html",
            {"form": NewEmailProfileForm, "title": "почту"},
        )
    elif request.method == "POST":
        form = NewEmailProfileForm(request.POST)
        user = User.objects.get(email=request.user.email)
        val = form.is_valid()
        if val:
            data = form.cleaned_data
            user.email = data["email"]
            user.save()
        return render(
            request,
            "profile_newdata.html",
            {
                "form": NewEmailProfileForm,
                "title": "почту",
                "formOld": form,
                "'val": val,
            },
        )


def NewUsernameProfile(request):
    if request.method == "GET":
        return render(
            request,
            "profile_newdata.html",
            {"form": NewUsernameProfileForm, "title": "ник"},
        )
    elif request.method == "POST":
        form = NewUsernameProfileForm(request.POST)
        user = User.objects.get(email=request.user.email)
        val = form.is_valid()
        if val:
            data = form.cleaned_data
            user.username = data["username"]
            user.save()
        return render(
            request,
            "profile_newdata.html",
            {
                "form": NewUsernameProfileForm,
                "title": "ник",
                "formOld": form,
                "val": val,
            },
        )


def NewFullNameProfile(request):
    if request.method == "GET":
        return render(
            request,
            "profile_newdata.html",
            {"form": NewFullNameProfileForm, "title": "имя и фамилию"},
        )
    elif request.method == "POST":
        form = NewFullNameProfileForm(request.POST)
        user = User.objects.get(email=request.user.email)
        val = form.is_valid()
        if val:
            data = form.cleaned_data
            user.first_name = data["first_name"]
            user.last_name = data["last_name"]
            user.save()
        return render(
            request,
            "profile_newdata.html",
            {
                "form": NewFullNameProfileForm,
                "title": "имя и фамилию",
                "formOld": form,
                "val": val,
            },
        )


def NewPhoneProfile(request):
    if request.method == "GET":
        return render(
            request,
            "profile_newdata.html",
            {"form": NewPhoneProfileForm, "title": "телефон"},
        )
    elif request.method == "POST":
        form = NewPhoneProfileForm(request.POST)
        user = User.objects.get(email=request.user.email)
        val = form.is_valid()
        if val:
            data = form.cleaned_data
            user.phone = data["phone"]
            user.save()
        return render(
            request,
            "profile_newdata.html",
            {
                "form": NewPhoneProfileForm,
                "title": "телефон",
                "formOld": form,
                "val": val,
            },
        )


def profile(request):
    return render(request, "profile.html")
