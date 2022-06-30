from django.db import models
from django.contrib.auth.models import User, Group

class Location(models.Model):
    name = models.CharField('Location Name', max_length = 120)
    address = models.CharField(max_length = 300)
    zip_code = models.CharField('Zip Code', max_length = 15)
    phone = models.CharField('Contact Phone', max_length = 25, blank = True)
    web = models.URLField('Website Address', blank = True)
    email_address = models.EmailField('Email Address', blank = True)
    location_image = models.ImageField(null = True, blank = True, upload_to="images/")

    def __str__(self):
        return self.name

class Event(models.Model):
    name = models.CharField('Event Name', max_length=120)
    event_date = models.DateTimeField('Event Date')
    location = models.ForeignKey(Location, blank = True, null = True, on_delete = models.CASCADE)
    manager = models.ForeignKey(Group, blank = True, null = True, on_delete= models.SET_NULL)
    description = models.TextField(blank = True)
    attendees = models.ManyToManyField(User, blank = True, null = True)

    def __str__(self):
        return self.name