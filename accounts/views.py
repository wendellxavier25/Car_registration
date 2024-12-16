from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login
from django.contrib import auth


def register(request):
    if request.method == "POST":
        user_form = UserCreationForm(request.POST)
        if user_form.is_valid():
            user_form.save()
            return redirect('accounts:login')
    else:
        user_form = UserCreationForm()
    return render(request, 'register.html', {'user_form': user_form, })


def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('car:cars_list')
        else:
            login_form = AuthenticationForm()

    else:
        login_form = AuthenticationForm()
    return render(request, 'login_view.html', {'login_form': login_form})


def logout_view(request):
    auth.logout(request)
    return redirect('car:cars_list')