# facturasieli/models/Company.py
from django.db import models
from facturasieli.models.Address import Address
from django.utils.translation import gettext_lazy as _

class Company(models.Model):
    siret = models.CharField(_("SIRET"), max_length=15)
    name = models.CharField(_("Name"), max_length=255)
    address = models.ForeignKey(Address, on_delete=models.CASCADE, related_name='companies')

    def __str__(self):
        return self.name
