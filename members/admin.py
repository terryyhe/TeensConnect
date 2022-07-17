from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import MemberCreationForm, MemberChangeForm
from .models import Member


class MemberAdmin(UserAdmin):
    add_form = MemberCreationForm
    form = MemberChangeForm
    model = Member
    list_display = ('email', 'is_staff', 'is_active',)
    list_filter = ('email', 'is_staff', 'is_active', 'groups',)
    fieldsets = (
        (None, {'fields': ('email', 'password', 'groups')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active', 'groups')}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)


admin.site.register(Member, MemberAdmin)