from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('events', views.events, name='events'),
    path('other/<int:year>/<str:month>', views.other, name='other'),
    path('login', views.login_user, name='login'),
]