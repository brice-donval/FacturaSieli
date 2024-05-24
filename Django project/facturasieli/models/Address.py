# facturasieli/models/Address.py
from django.db import models


class Address(models.Model):
    number = models.IntegerField()
    street = models.CharField(max_length=255)
    addings = models.CharField(max_length=255, blank=True, null=True)
    zip_code = models.IntegerField()
    city = models.CharField(max_length=255)
    country = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.number} {self.street}, {self.city}, {self.country}'
