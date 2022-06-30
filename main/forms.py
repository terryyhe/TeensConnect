from django import forms
from django.forms import ModelForm
from .models import Location, Event

class LocationForm(ModelForm):
    class Meta:
        model = Location
        fields = ('name', 'address', 'zip_code', 'phone', 'web', 'email_address', 'location_image')
        labels = {
            'name': '',
            'address': '',
            'zip_code': '',
            'phone': '',
            'web': '',
            'email_address': '',
            'location_image': 'Image',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'location name'}),
            'address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'address'}),
            'zip_code': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'zip_code'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'phone'}),
            'web': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'web'}),
            'email_address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'email_address'}),
        }

class EventForm(ModelForm):
    class Meta:
        model = Event
        fields = ('name', 'event_date', 'location', 'manager', 'description', 'attendees')
        labels = {
            'name': '',
            'event_date': '',
            'location': 'Location',
            'manager': '',
            'description': '',
            'attendees': '',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Event name'}),
            'event_date': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Date'}),
            'location': forms.Select(attrs={'class': 'form-control'}),
            'manager': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Manager'}),
            'description': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Description'}),
            'attendees': forms.SelectMultiple(attrs={'class': 'form-control', 'placeholder': 'Attendees'}),
        }

