from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

from .forms import CreateUserForm

from django.contrib import messages


def registerPage(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for ' + user)

            return redirect('login')

    return render(request, "weather/register.html", {'form': form})


def index(request):
    return render(request, 'weather/index.html')


def login(request):
    return render(request, 'weather/login.html')
