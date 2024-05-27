# facturasieli/models/User.py
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.utils.translation import gettext_lazy as _

from facturasieli.models.Company import Company
from facturasieli.models.Role import Role


class User(AbstractBaseUser):
    objects = BaseUserManager()
    email = models.EmailField(_("Email"), unique=True)
    first_name = models.CharField(_("First Name"), max_length=150)
    last_name = models.CharField(_("Last Name"), max_length=150)
    creation_date = models.DateField(_("Creation Date"), auto_now_add=True)
    modification_date = models.DateField(_("Modification Date"), auto_now=True)
    password = models.CharField(_("Password"), max_length=255)
    role = models.ManyToManyField(Role, related_name='users')

    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='employees')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
