from django.urls import path
from . import views

urlpatterns = [
    path('login', views.login_member, name='login'),
    path('logout', views.logout_member, name='logout'),
    path('register_member', views.register_member, name='register_member'),
    path('view_member/<int:member_id>', views.view_member, name='view_member'),
    path('update_member/<int:member_id>', views.update_member, name='update_member'),
    path('members', views.list_members, name='list_members'),
    path('myprofile', views.myprofile, name='myprofile'),
]