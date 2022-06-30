from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import NewUserForm

def login_user(request):
    if request.method != 'POST':
        return render(request, 'authenticate/login.html', {})

    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect('home')
    else:
        messages.success(request, "There was an error login, try again...")
        return redirect('login')

def logout_user(request):
    logout(request)
    messages.success(request, ("You were logged out"))
    return redirect("home")

def register_user(request):
    if request.method == 'POST':
        form = NewUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username = username, password = password)
            login(request, user)
            messages.success(request, ("Registration Successful"))
            return redirect('home')
    else:
        form = NewUserForm()

    return render(request, 'authenticate/register_user.html', {'form': form})
    