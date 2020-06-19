from django.shortcuts import render, redirect, HttpResponse
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
# Create your views here.


def register(request):
    if request.user.is_authenticated:
        return redirect("home")
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, "Account was created successfully for " + user)
                return redirect("login")
    context = {'form': form}
    return render(request, 'accounts/register.html', context)


def register_referred(request, username):
    if request.user.is_authenticated:
        return redirect("home")
    else:
        referrer = User.objects.get(username=username)
        form = CreateUserForm()
        if request.method == "POST":
            form = CreateUserForm(request.POST)
            if form.is_valid():
                referred = form.save()
                Referral.objects.create(
                    referrer=referrer,
                    referred=referred
                )
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, "Account was created successfully for " + user +
                                 "referred by " + referrer.username)
                return redirect("login")
    context = {'form': form}
    return render(request, 'accounts/register.html', context)


def login_page(request):
    if request.user.is_authenticated:
        return redirect("home")
    else:
        if request.method == "POST":
            username = request.POST.get("username")
            password = request.POST.get("password")

            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                print(user)
                return redirect("home")
            else:
                print(user)
                messages.error(request, "Incorrect username or password")
                # return redirect("login")
    context = {}
    return render(request, 'accounts/login.html', context)


def logout_user(request):
    logout(request)
    return redirect("login")


@login_required(login_url="login")
def home_page(request):
    user = request.user
    print(user)
    return render(request, 'index.html', {'user': user})
