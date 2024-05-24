# facturasieli/models/Role.py
from django.db import models


class Role(models.Model):
    role = models.CharField(max_length=255)
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.role
