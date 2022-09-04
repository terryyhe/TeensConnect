from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('search', views.search_bar, name='search_bar'),
    path('list_calendar', views.list_calendar, name='list_calendar'),
    path('add_calendar', views.add_calendar, name='add_calendar'),
    path('events', views.list_events, name='list_events'),
    path('add_event', views.add_event, name='add_event'),
    path('update_event/<int:event_id>', views.update_event, name='update_event'),
    path('view_event/<int:event_id>', views.view_event, name='view_event'),
    path('delete_event/<int:event_id>', views.delete_event, name='delete_event'),
    path('locations', views.list_locations, name='list_locations'),
    path('add_location', views.add_location, name='add_location'),
    path('update_location/<int:location_id>', views.update_location, name='update_location'),
    path('delete_location/<int:location_id>', views.delete_location, name='delete_location'),
    path('galleries', views.list_galleries, name='list_galleries'),
    path('add_gallery', views.add_gallery, name='add_gallery'),
    path('update_gallery/<int:gallery_id>', views.update_gallery, name='update_gallery'),
    path('photos', views.list_photos, name='list_photos'),
    path('add_photo', views.add_photo, name='add_photo'),
    path('update_photo/<int:photo_id>', views.update_photo, name='update_photo'),
    path('team-art', views.team_art, name='team_art'),
    path('team-cs', views.team_cs, name='team_cs'),
    path('team-tutor', views.team_tutor, name='team_tutor'),
    path('team-man', views.team_management, name='team_management')
]
