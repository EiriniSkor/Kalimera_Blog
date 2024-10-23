from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse
from mainapp.forms import RegisterForm, LoginForm, MorningNotesForm
from .models import MorningNotes

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

# Custom Login View
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
    if request.method == 'POST':
        form = MorningNotesForm(request.POST)
        if form.is_valid():
            morning_note = form.save(commit=False)  # Do not save immediately
            morning_note.user = request.user  # Set the user to the current logged-in user
            morning_note.save()  # Now save it
            return redirect('mainapp:profile')  # Redirect to the same profile page
    else:
        form = MorningNotesForm()

    # Fetch existing morning notes (fix typo here)
    morning_notes = MorningNotes.objects.filter(user=request.user)

    return render(request, 'mainapp/profile.html', {'form': form, 'morning_notes': morning_notes})

# User Logout View
@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('mainapp:index'))
