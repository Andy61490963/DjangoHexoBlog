from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterUserForm

# Gobel background control
context = {'small_background': True}

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You were logged in successfully")
            request.session['small_background'] = True
            return redirect('Archives')
        else:
            messages.success(request, "Please try again...")
            request.session['small_background'] = True
            return redirect('login')

    else:
        return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    messages.success(request, "You were logged out")
    request.session['small_background'] = True
    return redirect('home')

def register_user(request):
    if request.method == "POST":
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "Registration successful. Welcome!")
            request.session['small_background'] = True
            return redirect('Archives')
        else:
            messages.error(request, "Registration failed, please try again.")
    else:
        form = RegisterUserForm()

    return render(request, 'register_user.html', {'form': form, **context})