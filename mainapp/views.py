from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse
from mainapp.forms import RegisterForm, LoginForm

# Home Page View
def index(request):
    return render(request, 'mainapp/index.html')

# User Registration View
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()  # Save the new user
            login(request, user)  # Automatically log them in after registering
            return redirect('mainapp:profile')  # Redirect to profile page
    else:
        form = RegisterForm()
    
    return render(request, 'mainapp/register.html', {'form': form})

# Custom Login View (optional, you can use Django's built-in login view instead)
def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('mainapp:profile')
            else:
                return render(request, 'mainapp/login.html', {'form': form, 'error': 'Invalid username or password'})
    else:
        form = LoginForm()

    return render(request, 'mainapp/login.html', {'form': form})

# User Profile View (accessible only when logged in)
@login_required
def profile(request):
    return render(request, 'mainapp/profile.html', {'user': request.user})

# User Logout View
@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('mainapp:index'))
