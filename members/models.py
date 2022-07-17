from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, Group
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from .managers import MemberManager


class Member(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('Email Address'), unique=True)
    firstname = models.CharField('Firstname', max_length = 128)
    lastname = models.CharField('Lastname', max_length = 128)
    phone_number = models.CharField('Phone Number', max_length = 50)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)
    groups = models.ManyToManyField(Group, null = True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['firstname', 'lastname']

    objects = MemberManager()

    def __str__(self):
        return self.email