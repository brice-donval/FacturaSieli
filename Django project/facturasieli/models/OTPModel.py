# facturasieli/models/OTPModel.py
from django.contrib.auth.models import User
from django.db import models

from facturasieli.models.utils import compute_expiration_timestamp


class OTPModel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    creation_timestamp = models.DateTimeField(auto_now_add=True)
    expiration_timestamp = models.DateTimeField(default=compute_expiration_timestamp)
    otp = models.CharField(max_length=10)

    def __str__(self):
        return self.user.username
