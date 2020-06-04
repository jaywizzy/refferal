from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import *
# Create your views here.


def register(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, "Account was created successfully for" + user)
            return redirect("login")
    context = {'form': form}
    return render(request, 'accounts/register.html', context)


def register_referred(request, username):
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
            messages.success(request, "Account was created successfully for" + user +
                             "referred by " + referrer.username)
            return redirect("login")
    context = {'form': form}
    return render(request, 'accounts/register.html', context)


def login(request):
    context = {}
    return render(request, 'accounts/login.html', context)
