from django import forms
from django.forms import ModelForm
from .models import Location, Event
from django.utils.text import slugify 
from photologue.models import Photo, Gallery
from datetime import datetime

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

class NewPhotoForm(ModelForm):
    class Meta:
        model = Photo
        #fields = '__all__'
        fields = ('title', 'caption', 'image', 'crop_from', 'is_public', 'effect')
        labels = {
            'title': '',
            'caption': '',
        }

        widgets = {
            'title': forms.TextInput(attrs={'class': 'required form-control', 'placeholder': 'Title'}),
            'caption': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Caption'}),
            'crop_from': forms.Select(attrs={'class': 'form-control'}),
        }

    def save(self, commit=True):
        photo = super(NewPhotoForm, self).save(commit = False)
        photo.date_added = datetime.now()
        photo.slug = slugify(photo.title)
        photo.save()
        return photo

class NewGalleryForm(ModelForm):
    class Meta:
        model = Gallery
        fields = '__all__'
        
        widgets = {
            'title': forms.TextInput(attrs={'class': 'required form-control', 'placeholder': 'Title'}),
            'slug': forms.TextInput(attrs={'class': 'required form-control', 'placeholder': 'Title Slug'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
        }