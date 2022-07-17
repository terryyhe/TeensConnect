from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import NewMemberForm

def myprofile(request):
    pass

def view_member(request, member_id):
    pass

def login_member(request):
    if request.method != 'POST':
        return render(request, 'authenticate/login.html', {})

    username = request.POST['username']
    password = request.POST['password']
    member = authenticate(request, username=username, password=password)
    if member is not None:
        login(request, member)
        return redirect('home')
    else:
        messages.success(request, "There was an error login, try again...")
        return redirect('login')

def logout_member(request):
    logout(request)
    messages.success(request, ("You were logged out"))
    return redirect("home")

def register_member(request):
    if request.method == 'POST':
        form = NewMemberForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data['email']
            password = form.cleaned_data['password1']
            member = authenticate(email = email, password = password)
            login(request, member)
            messages.success(request, ("Registration Successful"))
            return redirect('home')
    else:
        form = NewMemberForm()

    return render(request, 'authenticate/register_member.html', {'form': form})
    