from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('search', views.search_bar, name='search_bar'),
    path('events', views.list_events, name='list_events'),
    path('add_event', views.add_event, name='add_event'),
    path('update_event/<int:event_id>', views.update_event, name='update_event'),
    path('delete_event/<int:event_id>', views.delete_event, name='delete_event'),
    path('locations', views.list_locations, name='list_locations'),
    path('add_location', views.add_location, name='add_location'),
    path('update_location/<int:location_id>', views.update_location, name='update_location'),
    path('delete_location/<int:location_id>', views.delete_location, name='delete_location'),
]
