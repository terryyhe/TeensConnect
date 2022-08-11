from django.shortcuts import render, redirect
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import NewMemberForm, MemberChangeForm
from .models import Member

def myprofile(request):
    pass

@staff_member_required(login_url="/members/login")
def view_member(request, member_id):
    try:
        member = Member.objects.get(pk = member_id)
    except:
        messages.error(request, "We don't have this member")
        return redirect('list_members')
    return render(request, 'authenticate/view_member.html', {'member':member})

@staff_member_required(login_url="/members/login")
def update_member(request, member_id):
    try:
        member = Member.objects.get(pk = member_id)
    except:
        messages.error(request, "We don't have this member")
        return redirect('list_members')
    if request.POST:
        form = MemberChangeForm(request.POST, instance = member)
        if form.is_valid():
            form.save()
        messages.success(request, "You have successufly updated the member info")
        return redirect('list_members')
    else:
        form = MemberChangeForm(instance = member)
        return render(request, 'authenticate/update_member.html', {'member': member, 'form': form})

@staff_member_required(login_url="/members/login")
def list_members(request):
    members = Member.objects.all()
    return render(request, 'authenticate/members.html', {'members': members})

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

@login_required(login_url="/members/login")
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
            #login(request, member)
            messages.success(request, ("Registration Successful, please wait for approval"))
            return redirect('home')
    else:
        form = NewMemberForm()

    return render(request, 'authenticate/register_member.html', {'form': form})
    
