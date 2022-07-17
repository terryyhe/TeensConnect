from django.shortcuts import render, redirect
from django.contrib.admin.views.decorators import staff_member_required
from django.http import HttpResponse
import calendar
from calendar import HTMLCalendar
from datetime import datetime
from django.contrib import messages
from .models import Event, Location
from .forms import LocationForm, EventForm

def home(request):
    #messages.add_message(request, messages.INFO, 'Hello world.')
    return render(request, 'home.html', {})

def about(request):
    return render(request, 'about.html', {})

def search_bar(request):
    if request.method == 'POST':
        searched = request.POST['searched']
        locations = Location.objects.filter(name__contains = searched)
        events = Event.objects.filter(name__contains = searched)
        return render(request, 'search_bar.html', {'searched': searched, 'locations': locations, 'events': events})
    else:
        return render(request, 'search_bar.html', {})
    
def list_events(request):
    events = Event.objects.all()
    return render(request, 'events.html', {'events':events})

@staff_member_required(login_url="/members/login")
def add_event(request):
    if request.POST:
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('list_events')
    else:
        form = EventForm()
        return render(request, 'add_event.html', {'form': form})

@staff_member_required(login_url="/members/login")
def update_event(request, event_id):
    event = Event.objects.get(pk = event_id)
    if request.POST:
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            form.save()
        messages.success(request, "You have successufly updated the event")
        return redirect('list_events')
    else:
        form = EventForm(instance=event)
        return render(request, 'update_event.html', {'form':form, 'event':event})

def view_event(request, event_id):
    try:
        event = Event.objects.get(pk = event_id)
    except:
        messages.error(request, "You don't have this event")
        return redirect('list_events')
    return render(request, 'view_event.html', {'event':event})

@staff_member_required(login_url="/members/login")
def delete_event(request, event_id):
    event = Event.objects.get(pk = event_id)
    event.delete()
    messages.success(request, "The event has been deleted")
    return redirect('list_events')
    
def list_locations(request):
    locations = Location.objects.all()
    return render(request, 'locations.html', {'locations':locations})

@staff_member_required(login_url="/members/login")
def add_location(request):
    if request.POST:
        form = LocationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "You have successfully added a new location")
            return redirect("list_locations")
    else:
        form = LocationForm()
        return render(request, 'add_location.html', {'form':form})

@staff_member_required(login_url="/members/login")
def delete_location(request, location_id):
    location = Location.objects.get(pk = location_id)
    location.delete()
    messages.success(request, "The location has been deleted")
    return redirect('list_locations')

@staff_member_required(login_url="/members/login")
def update_location(request, location_id):
    location = Location.objects.get(pk = location_id)
    if request.POST:
        form = LocationForm(request.POST, request.FILES, instance = location)
        if form.is_valid():
            form.save()
        messages.success(request, "You have successufly updated the location")
        return redirect('list_locations')
    else:
        form = LocationForm(instance = location)
        return render(request, 'update_location.html', {'location': location, 'form': form})
