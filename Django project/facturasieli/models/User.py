# facturasieli/models/User.py
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

from facturasieli.models.Company import Company
from facturasieli.models.Role import Role


class User(AbstractBaseUser):
    objects = BaseUserManager()
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    creation_date = models.DateField(auto_now_add=True)
    modification_date = models.DateField(auto_now=True)
    password = models.CharField(max_length=255)
    role = models.ManyToManyField(Role, related_name='users')

    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='employees')

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
