from django.contrib.auth import login as auth_login
from django.contrib.auth.models import User
from django.db import transaction
from django.shortcuts import render, redirect

from .forms import RegisterForm
from .models import Profile


def register(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            d = form.cleaned_data
            with transaction.atomic():
                user = User.objects.create_user(
                    username=d['login'],
                    email=d['login'],
                    password=d['password'],
                )
                Profile.objects.create(
                    user=user,
                    name=d['name'],
                    age=d['age'],
                    work=d['work'],
                    hobby=d['hobby'],
                )
            auth_login(request, user)
            return redirect('home')
    else:
        form = RegisterForm()

    return render(request, 'register.html', {'register': form})
