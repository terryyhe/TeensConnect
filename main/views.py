from django.shortcuts import render, redirect
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
import calendar
from calendar import HTMLCalendar
from datetime import datetime
from django.contrib import messages
from photologue.models import Photo, Gallery
from .models import Event, Location
from .forms import LocationForm, EventForm, NewPhotoForm, NewGalleryForm, NewCalendarForm
from .calendar_API import getEvents, getFutureEvents

def home(request):
    photos = Gallery.objects.filter(title = 'Home').first().photos.all()
    active = photos[0] if photos else None
    events = getFutureEvents()
    return render(request, 'home.html', {'photos': photos, 'active': active, 'events': events[:5]})

def about(request):
    return render(request, 'about.html', {})

def search_bar(request):
    if request.method == 'POST':
        searched = request.POST['searched']
        locations = Location.objects.filter(name__contains = searched)
        events = Event.objects.filter(name__contains = searched)
        photos = Photo.objects.filter(title__contains = searched)
        
        return render(request, 'search_bar.html', {'searched': searched, 'locations': locations, 'events': events, 'photos': photos})
    else:
        return render(request, 'search_bar.html', {})
    
def list_events(request):
    events = Event.objects.all()
    return render(request, 'events.html', {'events':events})

def list_calendar(request):
    return render(request, 'events2.html', {'events':getFutureEvents()})

def add_calendar(request):
    form = NewCalendarForm
    return render(request, 'add_calendar.html', {'form':form})


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

def list_photos(request):
    photos = Photo.objects.all()
    return render(request, 'list_photos.html', {'photos': photos})

@login_required(login_url="/members/login")
def add_photo(request):
    if request.POST:
        form = NewPhotoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'You have added a new photo')
            return redirect('home')
    else:
        form = NewPhotoForm()
    return render(request, 'add_photo.html', {'form':form})

@login_required(login_url="/members/login")
def update_photo(request, photo_id):
    photo = Photo.objects.get(pk = photo_id)
    form = NewPhotoForm(request.POST or None, request.FILES or None, instance = photo)
    if form.is_valid():
        form.save()
        messages.success(request, "You have successfully updated the photo record")
        return redirect('photologue:photo-list')
    return render(request, 'update_photo.html', {'photo': photo, 'form': form})

def list_galleries(request):
    galleries = Gallery.objects.all()
    return render(request, 'list_galleries.html', {'galleries': galleries})

@login_required(login_url="/members/login")
def add_gallery(request):
    form = NewGalleryForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, 'You have added a new gallery')
        return redirect('photologue:gallery-list')
    return render(request, 'add_gallery.html', {'form':form})

@login_required(login_url="/members/login")
def update_gallery(request, gallery_id):
    gallery = Gallery.objects.get(pk = gallery_id)
    form = NewGalleryForm(request.POST or None, instance = gallery)
    if form.is_valid():
        form.save()
        messages.success(request, "You have successfully updated the gallery record")
        return redirect('photologue:gallery-list')
    return render(request, 'update_gallery.html', {'gallery': gallery, 'form': form})


def team_art(request):
    return render(request, 'team_art.html', {})

def team_cs(request):
    photos = Gallery.objects.filter(title = 'Home').first().photos.all()
    active = photos[0] if photos else None
    return render(request, 'team_cs.html', {'photos': photos, 'active': active})

def team_tutor(request):
    return render(request, 'team_tutor.html', {})

def team_management(request):
    return render(request, 'team_management.html', {})
