# facturasieli/models/Company.py
from django.db import models

from facturasieli.models.Address import Address


class Company(models.Model):
    siret = models.CharField(max_length=15)
    name = models.CharField(max_length=255)
    address = models.ForeignKey(Address, on_delete=models.CASCADE, related_name='companies')

    def __str__(self):
        return self.name
